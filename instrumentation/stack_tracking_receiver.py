from dis import opname
from types import FrameType
from bytecode import Bytecode
import inspect

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops

from typing import Any, Dict, List, Union
from typing_extensions import Literal

class StackElement(object):
  def __init__(self, concrete: Any, opcode: int, deps: List["StackElement"]):
    self.concrete = concrete
    self.opcode = opcode
    self.deps = deps

# newtype to track object IDs
class ObjectId(object):
  def __init__(self, id: int) -> None:
    self.id = id

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, ObjectId):
      return self.id == other.id
    return False

def get_instrumented_program_frame() -> FrameType:
  is_next_frame = False
  for frame_container in inspect.getouterframes(inspect.currentframe()):
    if is_next_frame:
      return frame_container.frame
    elif frame_container.function == "py_instrument_receiver":
      is_next_frame = True
  raise Exception("Frame in instrumented code not found")

class StackTrackingReceiver(EventReceiver):
  loop_stack: List[Any]
  function_call_stack: List[Any]
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver = False
  symbolic_stack: List[StackElement]
  frame_variables: Dict[Union[FrameType, int], Dict[str, StackElement]]
  pre_op_stack: List[Any]
  frame_stack: List[FrameType]

  def __init__(self) -> None:
    self.loop_stack = []
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.symbolic_stack = []
    self.frame_variables = {}
    self.pre_op_stack = []
    self.frame_stack = []
    super().__init__()

  def show_op_index(self, code_id: int, op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> str:
    return "op #" + str(op_index) + " (" + str(id_to_orig_bytecode[code_id][op_index]) + ")"

  def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> str:
    if isinstance(maybe_id, ObjectId):
      return "obj #" + str(maybe_id.id) + " (" + str(self.heap_object_tracking.get_by_id(maybe_id.id)) + ")"
    else:
      return str(maybe_id)

  def stringify_frame_id(self, frame_id: Union[FrameType, int]) -> str:
    return "frame #" + str(frame_id)# + " (" + str(self.frame_tracking.get_by_id(frame_id)) + ")"

  def print_stack_indent(self) -> None:
    print("\t" * (len(self.loop_stack) + len(self.function_call_stack)), end="")

  def handle_jump_target(self, code_id: int, target_op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if target_op_index in self.loop_stack:
      while self.loop_stack[-1] != target_op_index:
        del self.loop_stack[-1]
      del self.loop_stack[-1] # drop the last element for real

      self.print_stack_indent()
      print("end loop")
    else:
      self.print_stack_indent()
      print("arrived at:", self.show_op_index(code_id, target_op_index, id_to_orig_bytecode))

  def convert_stack_elem_to_heap_id(self, elem: Any) -> Any:
    if self.heap_object_tracking.is_heap_object(elem):
      return ObjectId(self.heap_object_tracking.get_object_id(elem))
    else:
      return elem

  def convert_stack_to_heap_id(self, stack: List[Any]) -> List[Any]:
    object_id_stack = []
    for elem in stack:
      object_id_stack.append(self.convert_stack_elem_to_heap_id(elem))

    return object_id_stack

  def get_var_reference_frame(self, cur_frame: FrameType, arg: Any) -> Union[FrameType, int]:
    if "cell" in arg:
      return self.frame_tracking.get_object_id(cur_frame)
    else:
      fn_object = self.heap_object_tracking.get_by_id(self.function_call_stack[-1].id)
      cell_vars = fn_object.__code__.co_cellvars
      free_vars = fn_object.__code__.co_freevars
      var_index = free_vars.index(arg["free"])
      cell = fn_object.__closure__[var_index]
      return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]

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
          self.frame_variables[cur_frame][local] = StackElement(
            self.convert_stack_elem_to_heap_id(value),
            opcode, []
          )
      else:
        # TODO(shadaj): pop the args off the stack
        for local, value in cur_frame.f_locals.items():
          self.frame_variables[cur_frame][local] = StackElement(
            self.convert_stack_elem_to_heap_id(value),
            opcode, []
          )

    if opcode == "JUMP_TARGET":
      self.handle_jump_target(code_id, arg["label"], id_to_orig_bytecode)
    elif opname[opcode] == "CALL_FUNCTION":
      if not is_post:
        self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - len(stack)]

        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        self.print_stack_indent()
        print(
          "begin function call - function:",
          self.stringify_maybe_object_id(function_args_id_stack[0]),
          "on args",
          "(" + ", ".join(map(self.stringify_maybe_object_id, stack[1:])) + ")"
        )

        self.function_call_stack.append(function_args_id_stack[0])
      else:
        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        called_function = self.function_call_stack[-1]
        del self.function_call_stack[-1]

        # TODO(shadaj): the return value should be already there as long as the target function is instrumented / modeled
        self.symbolic_stack.append(StackElement(
          function_args_id_stack[0],
          opcode,
          [] # TODO(shadaj): return value does have dependencies
        ))

        self.print_stack_indent()
        print(
          "end function call - function:",
          self.stringify_maybe_object_id(called_function),
          "result:",
          self.stringify_maybe_object_id(function_args_id_stack[0])
        )
    elif opname[opcode] == "RETURN_VALUE":
      self.frame_stack.pop()
      self.print_stack_indent()
      print(f"return value -> {self.stringify_maybe_object_id(stack[0])}")
      if len(self.frame_stack) > 0 and not self.frame_stack[-1] == cur_frame.f_back:
        # this frame was called from a non-instrumented frame, so we drop the return value
        # if there is no frame on the stack, then we are at the top level, so we don't drop the return value
        self.symbolic_stack.pop()
      else:
        # TODO(shadaj): do not pop here once we can handle the return value in the parent
        if len(self.frame_stack) > 0:
          self.symbolic_stack.pop()
    else:
      object_id_stack = self.convert_stack_to_heap_id(stack)

      if not is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

      if opname[opcode] in binary_ops:
        if not is_post:
          tos = self.symbolic_stack.pop()
          tos1 = self.symbolic_stack.pop()
          self.pre_op_stack.append((tos1, tos))
        else:
          cur_inputs = self.pre_op_stack.pop()

          self.symbolic_stack.append(StackElement(
            object_id_stack[0],
            opcode,
            [cur_inputs[0], cur_inputs[1]]
          ))

          self.print_stack_indent()
          print(
            "binary op", self.stringify_maybe_object_id(cur_inputs[0].concrete), opname[opcode], self.stringify_maybe_object_id(cur_inputs[1].concrete),
            "->", self.stringify_maybe_object_id(object_id_stack[0])
          )
      elif opname[opcode] == "POP_TOP" or opname[opcode] == "POP_JUMP_IF_FALSE" or opname[opcode] == "POP_JUMP_IF_TRUE":
        if not is_post:
          self.print_stack_indent()
          print(f"pop top -> {self.stringify_maybe_object_id(stack[0])}")
          self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - 1]
      elif opname[opcode] == "ROT_TWO":
        tos = self.symbolic_stack.pop()
        tos1 = self.symbolic_stack.pop()
        self.symbolic_stack.append(tos)
        self.symbolic_stack.append(tos1)
      elif opname[opcode] == "LOAD_CONST":
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))

        self.print_stack_indent()
        print(
          "load const ->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_GLOBAL":
        # TODO(shadaj): implement correctly
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))

        self.print_stack_indent()
        print(
          "load global ->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        if arg in self.frame_variables[cur_frame]:
          if not self.frame_variables[cur_frame][arg].concrete == object_id_stack[0]:
            raise Exception(
              "Variable " + arg + " has changed from " + \
                self.stringify_maybe_object_id(self.frame_variables[cur_frame][arg].concrete) + \
                  " to " + self.stringify_maybe_object_id(object_id_stack[0]))
        else:
          raise Exception(f"Cannot create tracing value for previously unseen variable {arg} in {self.stringify_frame_id(self.frame_tracking.get_object_id(cur_frame))}")

        self.symbolic_stack.append(self.frame_variables[cur_frame][arg])

        self.print_stack_indent()
        print(
          "load", arg,
          "from", self.stringify_frame_id(self.frame_tracking.get_object_id(cur_frame)),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        cur_frame = get_instrumented_program_frame()
        if cur_frame not in self.frame_variables:
          self.frame_variables[cur_frame] = {}
        self.frame_variables[cur_frame][arg] = self.symbolic_stack.pop()

        self.print_stack_indent()
        print(
          "store", arg,
          "in", self.stringify_frame_id(self.frame_tracking.get_object_id(cur_frame)),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_SUBSCR":
        self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - 3]

        self.print_stack_indent()
        print(
          "store into", self.stringify_maybe_object_id(object_id_stack[1]),
          "at index", self.stringify_maybe_object_id(object_id_stack[2]),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "SETUP_LOOP":
        self.print_stack_indent()
        print("begin loop", id_to_orig_bytecode[code_id][opindex])
        self.loop_stack.append(arg["label"])
      elif opname[opcode] == "LOAD_CLOSURE":
        cur_frame = get_instrumented_program_frame()
        if not object_id_stack[0].id in self.cell_to_frame:
          self.cell_to_frame[object_id_stack[0].id] = self.frame_tracking.get_object_id(cur_frame)
          self.print_stack_indent()
          print(
            "prepare closure cell for variable " + arg["cell"] +
            " in " + self.stringify_frame_id(self.cell_to_frame[object_id_stack[0].id]) +
            " -> " + self.stringify_maybe_object_id(object_id_stack[0])
          )
      elif opname[opcode] == "LOAD_DEREF":
        cur_frame = get_instrumented_program_frame()
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.print_stack_indent()
        print(
          "load", var_name,
          "from", self.stringify_frame_id(resolved_frame),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_DEREF":
        cur_frame = get_instrumented_program_frame()
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.print_stack_indent()
        print(
          "store", var_name,
          "in", self.stringify_frame_id(resolved_frame),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      else:
        self.print_stack_indent()
        print("UNKNOWN OPCODE:")
        self.print_stack_indent()
        print("stack:", stack, "| opcode:", opname[opcode], "| arg:", arg, "| orig op:", id_to_orig_bytecode[code_id][opindex])
        # raise NotImplementedError()
      
      if is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

    self.already_in_receiver = False

  def check_symbolic_stack(self, object_id_stack: List[Any], opcode: int) -> None:
    for i, e in enumerate(object_id_stack):
      index_from_end = i - len(object_id_stack)
      if not self.symbolic_stack[index_from_end].concrete == e:
        print(opname[opcode])
        print([self.stringify_maybe_object_id(e.concrete) for e in self.symbolic_stack])
        print([self.stringify_maybe_object_id(e) for e in object_id_stack])
        raise Exception(
          "Stack element " + str(i) + " is symbolically " + \
            self.stringify_maybe_object_id(self.symbolic_stack[index_from_end].concrete) + \
              " but concretely " + self.stringify_maybe_object_id(e))
