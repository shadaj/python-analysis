
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

from .data_tracing_variables import *

from .memory_graph_generator import *

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

  def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
    super().__exit__(exc_type, exc_val, exc_tb)
    generate_memory_graph()

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
      assert cur_frame not in self.frame_variables, "Cannot reenter a previously exited context"
      self.frame_variables[cur_frame] = {}

      # frameId used for visualization only
      frameId = self.frame_tracking.get_object_id(cur_frame)

      if len(self.frame_stack) == 1 or not self.frame_stack[-2] == cur_frame.f_back:
        # this frame was called from a non-instrumented frame, or is the top-level frame,
        # so we have to populate locals without symbolic traces
        for local, value in cur_frame.f_locals.items():
          valueHeap = getHeapElement(value, self.heap_object_tracking)
          self.frame_variables[cur_frame][local] = SymbolicElement("\'\'\'%s|%s"%("frame%d"%frameId,local), valueHeap)
      else:
        for name, value in self.pre_op_stack[-1].arg_mapping.items():
          assert isinstance(value, StackElement), "Expected StackElement Instance"
          self.frame_variables[cur_frame][name] = SymbolicElement("\'\'\'%s|%s"%("frame%d"%frameId,name), value)
          #self.frame_variables[cur_frame][name] = StackElementVersion(StackElementFactory.getStackElement(value.fetch().concrete, opcode))
          add_dependency(self.frame_variables[cur_frame][name], value)
          #add_dependency_not_on_stack(self.frame_variables[cur_frame][name], value)

        # handle default arguments
        for local, value in cur_frame.f_locals.items():
          if local not in self.frame_variables[cur_frame]:
            # TODO(shadaj): handle mutable default arguments
            valueHeap = getHeapElement(value, self.heap_object_tracking)
            self.frame_variables[cur_frame][local] = SymbolicElement("\'\'\'%s|%s"%("frame%d"%frameId,local), valueHeap)

    # frameId used for visualization only
    frameId = self.frame_tracking.get_object_id(cur_frame)

    if opcode == "JUMP_TARGET":
      pass
    elif opname[opcode] == "CALL_FUNCTION" or opname[opcode] == "CALL_METHOD":
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

        # TODO: Uninstrumentable function dependencies where None is returned:
        if function_object == list.append:
          assert len(symbolic_stack_args) == 2, "Unexpected number of function call parameters" #self and object to append
          mainList = symbolic_stack_args[0]
          toAppend = symbolic_stack_args[1]
          mainList.heap_elem.collection_counter += 1
          currentCount = mainList.heap_elem.collection_counter
          currentPrefix = mainList.heap_elem.collection_prefix
          toAppendSymbolic = SymbolicElement(currentPrefix%(currentCount), toAppend)
          mainList.heap_elem.collection_heap_elems.append(toAppendSymbolic)
          add_dependency(toAppendSymbolic, toAppend)
      else:
        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        assert len(stack) == 1, "Expect one return value for any function"
        called_function = self.function_call_stack.pop()
        pre_op_stack_last_element = self.pre_op_stack.pop()
        return_on_stack = pre_op_stack_last_element.return_on_stack
        if return_on_stack:
          return_value_stack_el = self.symbolic_stack[0]
          assert isinstance(return_value_stack_el, StackElement), "Expected type mismatch"
        else:
          # TODO: Uninstrumentable function dependencies where return value helps infer dependencies
          if False: # Some method
            pass
          else: # Generic function
            return_value_heap = getHeapElement(stack[0],self.heap_object_tracking)
            return_value_stack_el = StackElement(return_value_heap)
            #StackElementVersion(StackElementFactory.getStackElement(function_ret_stack[0], opcode))
            self.symbolic_stack.append(return_value_stack_el)
          


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
      elif opname[opcode] == "ROT_THREE":
        tos = self.symbolic_stack.pop()
        tos1 = self.symbolic_stack.pop()
        tos2 = self.symbolic_stack.pop()
        self.symbolic_stack.append(tos)
        self.symbolic_stack.append(tos2)
        self.symbolic_stack.append(tos1)
      elif opname[opcode] == "DUP_TOP_TWO":
        tos = self.symbolic_stack.pop()
        tos2 = self.symbolic_stack.pop()
        tos_copy = tos.duplicate()
        tos2_copy = tos2.duplicate()
        self.symbolic_stack.append(tos2_copy)
        self.symbolic_stack.append(tos_copy)
        self.symbolic_stack.append(tos2)
        self.symbolic_stack.append(tos)
      elif opname[opcode] == "DUP_TOP":
        tos = self.symbolic_stack.pop()
        tos_copy = tos.duplicate()
        self.symbolic_stack.append(tos_copy)
        self.symbolic_stack.append(tos)
      elif opname[opcode] == "LOAD_CONST":
        assert is_post
        assert len(stack) == 1, "Only one const loaded at a time"
        self.symbolic_stack.append(StackElement(object_id_stack[0]))
        # NO REAL NEED FOR A NAME HERE AS IT IS JUST A CONST
      elif opname[opcode] == "LOAD_GLOBAL":
        # TODO(shadaj): implement correctly
        assert is_post
        if arg not in self.global_variables:
          self.global_variables[arg] = SymbolicElement("\'%s"%(arg), object_id_stack[0])
        assert isinstance(self.global_variables[arg], SymbolicElement), "Type mismatch"
        stackVal = StackElement(self.global_variables[arg])
        self.symbolic_stack.append(stackVal)
        add_dependency(stackVal, self.global_variables[arg])
      elif opname[opcode] == "LOAD_METHOD":
        assert is_post
        methodHeapId = object_id_stack[-2]
        selfStackElement = self.symbolic_stack.pop()
        assert isinstance(methodHeapId, HeapElement), "Type mismatch"
        methodStackElement = StackElement(methodHeapId)
        self.symbolic_stack.append(methodStackElement)
        self.symbolic_stack.append(selfStackElement)
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        assert is_post
        assert isinstance(self.frame_variables[cur_frame][arg], SymbolicElement), "Type mismatch"
        stackVal = StackElement(self.frame_variables[cur_frame][arg])
        self.symbolic_stack.append(stackVal)
        add_dependency(stackVal, self.frame_variables[cur_frame][arg])
        assert object_id_stack[0] == stackVal.heap_elem, "This variable got modified at an unknown position"
      elif opname[opcode] == "GET_ITER":
        assert is_post
        self.symbolic_stack.pop() #Popping the original collection from symbolic stack
        # The concrete stack actually has an iter object however which gets popped automatically when iterator exhausts
        #
        # We do not add any symbolic stac element for the iterator as it is not accessed otherwise. GET_ITER is always followed 
        # by FOR_ITER which would pop the iterator
      elif opname[opcode] == "FOR_ITER":
        assert is_post
        iterateHeapValue = object_id_stack[-1]
        iterateStackElement = StackElement(iterateHeapValue)
        self.symbolic_stack.append(iterateStackElement)
        # See GET_ITER notes
      elif opname[opcode] == "BUILD_LIST" or opname[opcode] == "BUILD_SLICE" or opname[opcode] == "BUILD_TUPLE":
        assert is_post
        newListHeap = object_id_stack[0]
        newListSymStack = StackElement(newListHeap)
        # TODO TODO TODO: Constructor dependencies
        # for i in range(int(arg)):
        #   add_dependency(newListSymStack, self.symbolic_stack[- i - 1])
        self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - int(arg)]
        self.symbolic_stack.append(newListSymStack)  
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        #######
        # TODO: AAYAN: IF LIST + SLICE, NEW STACKELEMENTS MAY BE INTRODUCED
        # ELSE: JUST ADD DEPENDENCY FROM LOADED SYMBOLIC LHS TO SYMBOLIC RHS
        #######
        #### IF A COLLECTION, CHANGE THE THING IT IS POINTING TO
        assert not is_post
        stackVal = self.symbolic_stack.pop()
        if arg not in self.frame_variables[cur_frame]:
          self.frame_variables[cur_frame][arg] = SymbolicElement("\'\'\'%s|%s"%("frame%d"%frameId,arg), stackVal)
        symbVal = self.frame_variables[cur_frame][arg]
        assert isinstance(symbVal, SymbolicElement), "Type mismatch"
        assert isinstance(stackVal, StackElement), "Type mismatch"
        # symbVal.heap_elem = stackVal.heap_elem ALREADY HANDLED INSIDE ADD_DEPENDENCY
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

          
          #if collection.is_cow_pointer and collection.cow_latest_value and collection.cow_latest_value.collection_elems:
          if hasattr(collection.heap_elem, "collection_heap_elems"):
            #TODO: Handle case if there may be side effects caused by custom __index__ for custom objects
            if not self.heap_object_tracking.is_heap_object(index.heap_elem.object_id):
              index_reified = index.heap_elem.object_id
              nameless_symbolic_element = collection.heap_elem.collection_heap_elems[index_reified]
              #loaded_heap_element_at_index = collection.heap_elem.collection_heap_elems[index_reified]
              assert isinstance(nameless_symbolic_element, SymbolicElement)
              stackElem = StackElement(nameless_symbolic_element)
              self.symbolic_stack.append(stackElem)
              add_dependency(stackElem, nameless_symbolic_element)
            else:
              index_reified = self.heap_object_tracking.get_by_id(index.heap_elem.object_id.id)
              nameless_symbolic_elements = collection.heap_elem.collection_heap_elems[index_reified]
              sliceHeap = object_id_stack[0]
              sliceStackEl = StackElement(sliceHeap)
              assert len(nameless_symbolic_elements) == len(sliceStackEl.heap_elem.collection_heap_elems), "Concrete and symbolic arrays should be of the same size"
              self.symbolic_stack.append(sliceStackEl)
              for i in range(len(nameless_symbolic_elements)):
                add_dependency(sliceStackEl.heap_elem.collection_heap_elems[i], nameless_symbolic_elements[i])
            
          else:
            raise Exception("expected collection")
            #Exception(f"Cannot store into non-cow collection: {self.stringify_maybe_object_id(collection.concrete)}")
      elif opname[opcode] == "STORE_SUBSCR":
        index = self.symbolic_stack.pop()
        collection = self.symbolic_stack.pop()
        value = self.symbolic_stack.pop()
        
        # TODO:Handle the splice case for list when list size changes. splice intoduces a new array symbolically
        if not self.heap_object_tracking.is_heap_object(index.heap_elem.object_id):
          index_reified = index.heap_elem.object_id # TODO(shadaj): handle non-integer indices
          nameless_symbolic_element = collection.heap_elem.collection_heap_elems[index_reified]
          #loaded_heap_element_at_index = collection.heap_elem.collection_heap_elems[index_reified]
          assert isinstance(nameless_symbolic_element, SymbolicElement)
          add_dependency(nameless_symbolic_element, value)
        else:
          index_reified = self.heap_object_tracking.get_by_id(index.heap_elem.object_id.id)
          nameless_symbolic_elements = collection.heap_elem.collection_heap_elems[index_reified]
          assert len(nameless_symbolic_elements) == len(value.heap_elem.collection_heap_elems), "Concrete and symbolic arrays should be of the same size"
          for i in range(len(nameless_symbolic_elements)):
            add_dependency(value.heap_elem.collection_heap_elems[i], nameless_symbolic_elements[i])
        #TODO: Store the Symbolic element in ollection?
        #symbElem = SymbolicElement(collection.heap_elem.object_id.__str__(), loaded_heap_element_at_index)
        # collection.heap_elem.collection_heap_elems[index_reified] = value.heap_elem
        
        
        #nameless_symbolic_element.heap_elem = value.heap_elem ALREADY HANDLED INSIDE ADD_DEPENDENCY
        
        
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
      elif opname[opcode] == "UNPACK_SEQUENCE":
        assert not is_post
        numElements = int(arg)
        sequenceSym = self.symbolic_stack.pop()
        assert numElements == len(sequenceSym.heap_elem.collection_heap_elems)
        for i in range(numElements):
          self.symbolic_stack.append(StackElement(sequenceSym.heap_elem.collection_heap_elems[- i - 1]))
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
