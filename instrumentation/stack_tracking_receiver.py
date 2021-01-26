from dis import opname
import inspect

from .heap_object_tracking import HeapObjectTracker

# newtype to track object IDs
class ObjectId(object):
  def __init__(self, id):
    self.id = id

class StackTrackingReceiver(object):
  def __init__(self):
    self.loop_stack = []
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}

  def show_op_index(self, code_id, op_index, id_to_orig_bytecode):
    return "op #" + str(op_index) + " (" + str(id_to_orig_bytecode[code_id][op_index]) + ")"

  def stringify_maybe_object_id(self, maybe_id):
    if isinstance(maybe_id, ObjectId):
      return "obj #" + str(maybe_id.id) + " (" + str(self.heap_object_tracking.get_by_id(maybe_id.id)) + ")"
    else:
      return str(maybe_id)

  def stringify_frame_id(self, frame_id):
    return "frame #" + str(frame_id)# + " (" + str(self.frame_tracking.get_by_id(frame_id)) + ")"

  def print_stack_indent(self):
    print("\t" * (len(self.loop_stack) + len(self.function_call_stack)), end="")

  def handle_jump_target(self, code_id, target_op_index, id_to_orig_bytecode):
    if target_op_index in self.loop_stack:
      while self.loop_stack[-1] != target_op_index:
        del self.loop_stack[-1]
      del self.loop_stack[-1] # drop the last element for real

      self.print_stack_indent()
      print("end loop")
    else:
      self.print_stack_indent()
      print("arrived at:", self.show_op_index(code_id, target_op_index, id_to_orig_bytecode))

  def convert_stack_to_heap_id(self, stack):
    object_id_stack = []
    for elem in stack:
      if self.heap_object_tracking.is_heap_object(elem):
        object_id_stack.append(ObjectId(self.heap_object_tracking.get_object_id(elem)))
      else:
        object_id_stack.append(elem)

    return object_id_stack

  def get_var_reference_frame(self, cur_frame, arg):
    if "cell" in arg:
      return self.frame_tracking.get_object_id(cur_frame.frame)
    else:
      fn_object = self.heap_object_tracking.get_by_id(self.function_call_stack[-1].id)
      cell_vars = fn_object.__code__.co_cellvars
      free_vars = fn_object.__code__.co_freevars
      var_index = free_vars.index(arg["free"])
      cell = fn_object.__closure__[var_index]
      return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]

  def __call__(self, stack, opcode, arg, opindex, code_id, is_post, id_to_orig_bytecode):
    if opcode == "JUMP_TARGET":
      self.handle_jump_target(code_id, arg["label"], id_to_orig_bytecode)
    elif opname[opcode] == "CALL_FUNCTION" and not is_post:
      function_args_id_stack = self.convert_stack_to_heap_id(stack)
      self.print_stack_indent()
      print(
        "begin function call - function:",
        self.stringify_maybe_object_id(function_args_id_stack[0]),
        "on args",
        "(" + ", ".join(map(self.stringify_maybe_object_id, stack[1:])) + ")"
      )

      self.function_call_stack.append(function_args_id_stack[0])
    elif opname[opcode] == "CALL_FUNCTION" and is_post:
      function_args_id_stack = self.convert_stack_to_heap_id(stack)
      called_function = self.function_call_stack[-1]
      del self.function_call_stack[-1]

      self.print_stack_indent()
      print(
        "end function call - function:",
        self.stringify_maybe_object_id(called_function),
        "result:",
        self.stringify_maybe_object_id(function_args_id_stack[0])
      )
    elif opname[opcode] == "BINARY_SUBSCR":
      object_id_stack = self.convert_stack_to_heap_id(stack)
      if not is_post:
        self.cur_load = (object_id_stack[0], object_id_stack[1])
      else:
        self.print_stack_indent()
        print(
          "load", self.stringify_maybe_object_id(self.cur_load[0]), "at index", self.stringify_maybe_object_id(self.cur_load[1]),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
    else:
      object_id_stack = self.convert_stack_to_heap_id(stack)

      if opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        self.print_stack_indent()
        print(
          "load", arg,
          "from", self.stringify_frame_id(self.frame_tracking.get_object_id(
            inspect.getouterframes(inspect.currentframe())[1].frame
          )),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        self.print_stack_indent()
        print(
          "store", arg,
          "in", self.stringify_frame_id(self.frame_tracking.get_object_id(
            inspect.getouterframes(inspect.currentframe())[1].frame
          )),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_SUBSCR":
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
        cur_frame = inspect.getouterframes(inspect.currentframe())[1]
        if not object_id_stack[0].id in self.cell_to_frame:
          self.cell_to_frame[object_id_stack[0].id] = self.frame_tracking.get_object_id(cur_frame.frame)
          self.print_stack_indent()
          print(
            "prepare closure cell for variable " + arg["cell"] +
            " in " + self.stringify_frame_id(self.cell_to_frame[object_id_stack[0].id]) +
            " -> " + self.stringify_maybe_object_id(object_id_stack[0])
          )
      elif opname[opcode] == "LOAD_DEREF":
        cur_frame = inspect.getouterframes(inspect.currentframe())[1]
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.print_stack_indent()
        print(
          "load", var_name,
          "from", self.stringify_frame_id(resolved_frame),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_DEREF":
        cur_frame = inspect.getouterframes(inspect.currentframe())[1]
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
