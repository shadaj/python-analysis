from __future__ import annotations

from dis import opname, opmap
from sys import version
from types import FrameType
from bytecode import Bytecode
import inspect

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops
from .util import ObjectId, get_instrumented_program_frame

from typing import Any, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal

def add_dependency(child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  print("New dependency: ")
  print("Child: ", str(child))
  print("Parent: ", str(parent))
  child.heap_elem = parent.heap_elem
  child.version = 1 + max(child.version, parent.version)

def add_dependency2(child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement]) -> None:
  print("New dependency: ")
  print("Child: ", str(child))
  print("Parent1: ", str(parent1))
  print("Parent2: ", str(parent2))
  child.version = 1 + max(child.version, parent1.version, parent2.version)

object_id_to_heap_element_map: Dict[Union[ObjectId, int, str], HeapElement] = {}
def getHeapElement(concrete: Any, heap_object_tracker: HeapObjectTracker) -> HeapElement:
  if heap_object_tracker.is_heap_object(concrete):
    key = ObjectId(heap_object_tracker.get_object_id(concrete))
  else:
    key = concrete
  if key not in object_id_to_heap_element_map:
    object_id_to_heap_element_map[key] = HeapElement(concrete, heap_object_tracker)
  return object_id_to_heap_element_map[key]
  

class HeapElement(object):
  object_id: Union[ObjectId, int, str]
  collection_heap_elems: Optional[Union[List["HeapElement"], Dict["HeapElement", "HeapElement"]]] 

  def __init__(self, concrete: Any, heap_object_tracker: HeapObjectTracker) -> None:
    assert not isinstance(concrete, HeapElement), "Did not expect a HeapElement here"
    if heap_object_tracker.is_heap_object(concrete):
      self.object_id = ObjectId(heap_object_tracker.get_object_id(concrete))
      if isinstance(concrete, list):
        self.collection_heap_elems = [getHeapElement(e, heap_object_tracker) for e in concrete]
      elif isinstance(concrete, dict):
        raise Exception("Not handled HeapElements for dicts")
    else:
      assert isinstance(concrete, (int, str)), "Unhandled data type"
      self.object_id = concrete #int or str

class SymbolicElement(object):
  var_name: str
  heap_elem: HeapElement
  version: int

  def __init__(self, var_name: str, elems: Union[HeapElement, StackElement], version = 0) -> None:
    if isinstance(elems, HeapElement):
      self.var_name = var_name
      self.heap_elem = elems
      self.version = version #Starting version of any symbolic element is zero
    elif isinstance(elems, StackElement):
      self.var_name = var_name
      self.heap_elem = elems.heap_elem 
      self.version = elems.version 
    else:
      raise Exception("Unexpected type")

class StackElement(object):
  heap_elem: HeapElement
  version: int

  def __init__(self, elems: Union[HeapElement, SymbolicElement], version = 0) -> None:
    if isinstance(elems, HeapElement):
      self.heap_elem = elems
      self.version = version #Starting version of any symbolic element is zero
    elif isinstance(elems, SymbolicElement):
      self.heap_elem = elems.heap_elem
      self.version = elems.version

class FunctionCallHandled(object):
  return_on_stack: bool
  arg_mapping: Dict[str, StackElement]

  def __init__(self, arg_mapping: Dict[str, StackElement]) -> None:
    self.return_on_stack = False
    self.arg_mapping = arg_mapping


class DataTracingReceiver(EventReceiver):
  function_call_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  frame_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  symbolic_stack: List[StackElement]
  frame_variables: Dict[Union[FrameType, int], Dict[str, SymbolicElement]]
  global_variables: Dict[str, SymbolicElement]
  pre_op_stack: List[Union[FunctionCallHandled, Tuple[StackElement, StackElement]]]
  frame_stack: List[FrameType]

  def __init__(self) -> None:
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.symbolic_stack = []
    self.frame_variables = {}
    self.global_variables = {}
    self.pre_op_stack = []
    self.frame_stack = []
    super().__init__()

  def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> str:
    if isinstance(maybe_id, ObjectId):
      return "obj #" + str(maybe_id.id) + " (" + str(self.heap_object_tracking.get_by_id(maybe_id.id)) + ")"
    else:
      return str(maybe_id)

  def stringify_frame_id(self, frame_id: Union[FrameType, int]) -> str:
    return "frame #" + str(frame_id)

  def convert_stack_to_heap_id(self, stack: List[Any]) -> List[HeapElement]:
    object_id_stack = []
    for elem in stack:
      object_id_stack.append(getHeapElement(elem, self.heap_object_tracking))
    return object_id_stack

  def get_var_reference_frame(self, cur_frame: FrameType, arg: Any) -> Union[FrameType, int]:
    assert False, "Not tested"
    if "cell" in arg:
      return self.frame_tracking.get_object_id(cur_frame)
    else:
      fn_object = self.heap_object_tracking.get_by_id(self.function_call_stack[-1].id)
      cell_vars = fn_object.__code__.co_cellvars
      free_vars = fn_object.__code__.co_freevars
      var_index = free_vars.index(arg["free"])
      cell = fn_object.__closure__[var_index]
      return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]

  ######################
  # MAIN EVENT HANDLER #
  ######################
  def on_event(self, stack: List[Any], opcode: Union[Literal["JUMP_TARGET"], int], arg: Any, opindex: int, code_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if self.already_in_receiver:
      return
    self.already_in_receiver = True
    
    cur_frame = get_instrumented_program_frame()
    if len(self.frame_stack) == 0 or not self.frame_stack[-1] == cur_frame:
      # first time entering this instrumented frame
      self.frame_stack.append(cur_frame)
      self.frame_variables[cur_frame] = {}

      if len(self.frame_stack) == 1 or not self.frame_stack[-2] == cur_frame.f_back:
        # this frame was called from a non-instrumented frame, or is the top-level frame,
        # so we have to populate locals without symbolic traces
        for local, value in cur_frame.f_locals.items():
          valueHeap = getHeapElement(value, self.heap_object_tracking)
          self.frame_variables[cur_frame][local] = SymbolicElement(local, valueHeap)
      else:
        for name, value in self.pre_op_stack[-1].arg_mapping.items():
          assert isinstance(value, StackElement), "Expected StackElement Instance"
          self.frame_variables[cur_frame][name] = SymbolicElement(name, value.heap_elem)
          #self.frame_variables[cur_frame][name] = StackElementVersion(StackElementFactory.getStackElement(value.fetch().concrete, opcode))
          add_dependency(self.frame_variables[cur_frame][name], value)
          #add_dependency_not_on_stack(self.frame_variables[cur_frame][name], value)

        # handle default arguments
        for local, value in cur_frame.f_locals.items():
          if local not in self.frame_variables[cur_frame]:
            # TODO(shadaj): handle mutable default arguments
            valueHeap = getHeapElement(value, self.heap_object_tracking)
            self.frame_variables[cur_frame][local] = SymbolicElement(local, valueHeap)

    if opcode == "JUMP_TARGET":
      pass
    elif opname[opcode] == "CALL_FUNCTION":
      if not is_post:
        symbolic_stack_args = self.symbolic_stack[len(self.symbolic_stack) - len(stack) + 1:]
        self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - len(stack)]

        function_args_id_stack = self.convert_stack_to_heap_id(stack)

        args_mapping = {}
        function_object = self.heap_object_tracking.get_by_id(function_args_id_stack[0].object_id.id)

        if hasattr(function_object, "__code__"):
          code_object = function_object.__code__
          positional_arg_names = list(code_object.co_varnames)[:code_object.co_argcount]
          # TODO(shadaj): handle non-positional calls
          for i, arg in enumerate(positional_arg_names):
            if i < len(symbolic_stack_args):
              args_mapping[arg] = symbolic_stack_args[i]

        self.function_call_stack.append(function_args_id_stack[0])
        self.pre_op_stack.append(FunctionCallHandled(args_mapping))
      else:
        assert len(stack) == 1, "Expect one return value for any function"
        called_function = self.function_call_stack.pop()
        pre_op_stack_last_element = self.pre_op_stack.pop()
        return_on_stack = pre_op_stack_last_element.return_on_stack
        if return_on_stack:
          return_value_stack_el = self.symbolic_stack[0]
          assert isinstance(return_value_stack_el, StackElement), "Expected type mismatch"
        else:
          # TODO: Dependencies to be added depending on the function itself. Currently this is an approximation might have to be changed
          return_value_heap = getHeapElement(stack[0],self.heap_object_tracking)
          return_value_stack_el = StackElement(return_value_heap)
          #StackElementVersion(StackElementFactory.getStackElement(function_ret_stack[0], opcode))
          self.symbolic_stack.append(return_value_stack_el)
          #self.symbolic_stack.append(return_value_symbolic)

        # TODO: Add Dependencie?
        # if not(stack[0] is None):
        #   add_dependency(return_value_stack_el, )

        # if not return_on_stack:
        #   assert False, "The un-instrumentable function decides the dependencies here, need to handle on per-function basis"
        #   self.symbolic_stack.append(StackElement(
        #     function_args_id_stack[0],
        #     opcode,
        #     [] # TODO(shadaj): add approximate dependencies
        #   ))
    elif opname[opcode] == "RETURN_VALUE":
      self.frame_stack.pop()
      # if there is no frame on the stack, then we are at the top level, so we don't drop the return value
      if len(self.frame_stack) > 0:
        if not self.frame_stack[-1] == cur_frame.f_back:
          # this frame was called from a non-instrumented frame, so we drop the return value
          self.symbolic_stack.pop()
        else:
          self.pre_op_stack[-1].return_on_stack = True
    else:
      object_id_stack = self.convert_stack_to_heap_id(stack)

      if not is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

      if opname[opcode] == "POP_TOP" or opname[opcode] == "POP_JUMP_IF_FALSE" or opname[opcode] == "POP_JUMP_IF_TRUE":
        if not is_post:
          self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - 1]
      elif opname[opcode] == "ROT_TWO":
        tos = self.symbolic_stack.pop()
        tos1 = self.symbolic_stack.pop()
        self.symbolic_stack.append(tos)
        self.symbolic_stack.append(tos1)
      elif opname[opcode] == "LOAD_CONST":
        assert is_post
        assert len(stack) == 1, "Only one const loaded at a time"
        self.symbolic_stack.append(StackElement(object_id_stack[0]))
        # NO REAL NEED FOR A NAME HERE AS IT IS JUST A CONST
      elif opname[opcode] == "LOAD_GLOBAL":
        # TODO(shadaj): implement correctly
        assert is_post
        if arg not in self.global_variables:
          self.global_variables[arg] = SymbolicElement("\'g", object_id_stack[0])
        assert isinstance(self.global_variables[arg], SymbolicElement), "Type mismatch"
        stackVal = StackElement(self.global_variables[arg])
        self.symbolic_stack.append(stackVal)
        add_dependency(stackVal, self.global_variables[arg])
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        assert is_post
        assert isinstance(self.frame_variables[cur_frame][arg], SymbolicElement), "Type mismatch"
        stackVal = StackElement(self.frame_variables[cur_frame][arg])
        self.symbolic_stack.append(stackVal)
        add_dependency(stackVal, self.frame_variables[cur_frame][arg])
        assert object_id_stack[0] == stackVal.heap_elem, "This variable got modified at an unknown position"
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        #######
        # TODO: AAYAN: IF LIST + SLICE, NEW STACKELEMENTS MAY BE INTRODUCED
        # ELSE: JUST ADD DEPENDENCY FROM LOADED SYMBOLIC LHS TO SYMBOLIC RHS
        #######
        #### IF A COLLECTION, CHANGE THE THING IT IS POINTING TO
        assert not is_post
        stackVal = self.symbolic_stack.pop()
        if arg not in self.frame_variables[cur_frame]:
          self.frame_variables[cur_frame][arg] = SymbolicElement(arg, stackVal.heap_elem)
        symbVal = self.frame_variables[cur_frame][arg]
        assert isinstance(symbVal, SymbolicElement), "Type mismatch"
        assert isinstance(stackVal, StackElement), "Type mismatch"
        symbVal.heap_elem = stackVal.heap_elem
        add_dependency(symbVal, stackVal)
      elif opname[opcode] == "LOAD_DEREF":
        assert False, "Havent checked"
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.load_onto_symbolic_stack(object_id_stack, resolved_frame, var_name)
      elif opname[opcode] == "STORE_DEREF":
        assert False, "Havent Checked"
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.store_from_symbolic_stack(resolved_frame, var_name)
      elif opname[opcode] == "BINARY_SUBSCR":
        if not is_post:
          index = self.symbolic_stack.pop()
          collection = self.symbolic_stack.pop()
          self.pre_op_stack.append((collection, index))
        else:
          collection, index = self.pre_op_stack.pop()

          index_reified = index.heap_elem.object_id
          #if collection.is_cow_pointer and collection.cow_latest_value and collection.cow_latest_value.collection_elems:
          if collection.heap_elem.collection_heap_elems:
            #TODO: Handle case if there may be side effects caused by custom __index__ for custom objects
            # TODO:Handle the splice case for list. splice intoduces a new array symbolically
            loaded_heap_element_at_index = collection.heap_elem.collection_heap_elems[index_reified]
            assert isinstance(loaded_heap_element_at_index, HeapElement)
            stackElem = StackElement(loaded_heap_element_at_index)
            self.symbolic_stack.append(stackElem)
          else:
            raise Exception("expected collection")
            #Exception(f"Cannot store into non-cow collection: {self.stringify_maybe_object_id(collection.concrete)}")
      elif opname[opcode] == "STORE_SUBSCR":
        index = self.symbolic_stack.pop()
        collection = self.symbolic_stack.pop()
        value = self.symbolic_stack.pop()

        index_reified = index.heap_elem.object_id # TODO(shadaj): handle non-integer indices
        loaded_heap_element_at_index = collection.heap_elem.collection_heap_elems[index_reified]
        assert isinstance(loaded_heap_element_at_index, HeapElement)
        #TODO: Store the Symbolic element in ollection?
        symbElem = SymbolicElement(collection.heap_elem.object_id.__str__(), loaded_heap_element_at_index)
        collection.heap_elem.collection_heap_elems[index_reified] = value.heap_elem
        add_dependency(symbElem, value)
        # if collection.is_cow_pointer and collection.cow_latest_value:
        # orig_collection = collection.cow_latest_value
        # new_collection = orig_collection.collection_updated(index_reified, value)
        # collection.cow_latest_value = new_collection
        #######
        #AAYAN: IF LIST + SLICE, NEW STACKELEMENTS MAY BE INTRODUCED
        # ELSE: JUST ADD DEPENDENCY FROM LOADED SYMBOLIC LHS TO SYMBOLIC RHS
        #######
        # else:
        #   raise Exception("Cannot store into non-cow collection")
      elif opname[opcode] == "LOAD_CLOSURE":
        assert False, "Not examined yet"
        if not object_id_stack[0].id in self.cell_to_frame:
          self.cell_to_frame[object_id_stack[0].id] = self.frame_tracking.get_object_id(cur_frame)
        assert False, "Change append call to symbolicstack"
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))
      elif opname[opcode] == "SETUP_LOOP":
        pass
      elif opname[opcode] in binary_ops:
        if not is_post:
          tos = self.symbolic_stack.pop()
          tos1 = self.symbolic_stack.pop()
          self.pre_op_stack.append((tos1, tos))
          ########
          # ONLY  IF the __op__ method is not defined on 1st argument
          ########
        else:
          cur_inputs = self.pre_op_stack.pop()

          ########
          # How to do this
          ########
          stackEl = StackElement(object_id_stack[0])
          self.symbolic_stack.append(stackEl)
          add_dependency2(stackEl, cur_inputs[0], cur_inputs[1])
      else:
        raise NotImplementedError(opname[opcode])
      
      if is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

    self.already_in_receiver = False

  def check_symbolic_stack(self, object_id_stack: List[Any], opcode: int) -> None:
    print(opname[opcode])
    print("symbolic:", [self.stringify_maybe_object_id(e.heap_elem.object_id) for e in self.symbolic_stack])
    print("concrete:", [self.stringify_maybe_object_id(e.object_id) for e in object_id_stack])
    for i, e in enumerate(object_id_stack):
      index_from_end = i - len(object_id_stack)
      try:
        if not self.symbolic_stack[index_from_end].heap_elem.object_id == e.object_id:
          print(opname[opcode])
          print("symbolic:", [self.stringify_maybe_object_id(e.heap_elem.object_id) for e in self.symbolic_stack])
          print("concrete:", [self.stringify_maybe_object_id(e.object_id) for e in object_id_stack])
          raise Exception(
            "Stack element " + str(i) + " is symbolically " + \
              self.stringify_maybe_object_id(self.symbolic_stack[index_from_end].heap_elem.object_id) + \
                " but concretely " + self.stringify_maybe_object_id(e.object_id))
      except IndexError:
        print(opname[opcode])
        print("symbolic:", [self.stringify_maybe_object_id(e.heap_elem.object_id) for e in self.symbolic_stack])
        print("concrete:", [self.stringify_maybe_object_id(e.object_id) for e in object_id_stack])
        raise Exception("Stack element at index " + str(i) + " is not in symbolic stack")
