from types import CodeType, LambdaType

from bytecode import Bytecode, CellVar, FreeVar, Instr, Label, UNSET

from instrumentation.helper import printDebug

from .util import clone_bytecode_empty_body

from typing import Any, Callable, Dict, Optional, Union, cast, Tuple
from typing_extensions import Literal

# Mappings from op to the size of the stack to report

ignore_ops = [
  "IMPORT_NAME",
  "IMPORT_FROM",
  "NOP",
  "HAVE_ARGUMENT",
  "RAISE_VARARGS", # If an exception is thrown, we terminate our analysis for now. TODO: work on partially created graph if uncaught.
]

binary_ops = {
  "BINARY_POWER":"2**",
  "BINARY_MULTIPLY":"2*",
  "BINARY_MATRIX_MULTIPLY":"2@",
  "BINARY_FLOOR_DIVIDE":"2//",
  "BINARY_TRUE_DIVIDE":"2/",
  "BINARY_MODULO":"2%",
  "BINARY_ADD":"2+",
  "BINARY_SUBTRACT":"2-",
  "BINARY_SUBSCR":"2[]",
  "BINARY_LSHIFT":"2<<",
  "BINARY_RSHIFT":"2>>",
  "BINARY_AND":"2&",
  "BINARY_XOR":"2^",
  "BINARY_OR":"2|",

  "COMPARE_OP":"2?",

  "INPLACE_POWER":"2**",
  "INPLACE_MULTIPLY":"2*",
  "INPLACE_MATRIX_MULTIPLY":"2@",
  "INPLACE_FLOOR_DIVIDE":"2//",
  "INPLACE_TRUE_DIVIDE":"2/",
  "INPLACE_MODULO":"2%",
  "INPLACE_ADD":"2+",
  "INPLACE_SUBTRACT":"2-",
  "INPLACE_LSHIFT":"2<<",
  "INPLACE_RSHIFT":"2>>",
  "INPLACE_AND":"2&",
  "INPLACE_XOR":"2^",
  "INPLACE_OR":"2|",
}

unary_ops = {
  "UNARY_POSITIVE":"1+",
  "UNARY_NEGATIVE":"1-",
  "UNARY_NOT":"1not",
  "UNARY_INVERT":"1~"
}

# Opcodes to instrument before they run
pre_opcode_instrument: Dict[str, Union[int, Callable[[Instr], int]]] = {
  "JUMP_ABSOLUTE": 0,
  "JUMP_FORWARD": 0,
  "SETUP_LOOP": 0,
  "STORE_NAME": 1,
  "STORE_FAST": 1,
  "STORE_DEREF": 1,
  # "STORE_ATTR": 2,
  "STORE_SUBSCR": 3,
  "POP_TOP": 1,
  "POP_JUMP_IF_TRUE": 1,
  "POP_JUMP_IF_FALSE": 1,
  "ROT_TWO": 2,
  "ROT_THREE": 3,
  "DUP_TOP_TWO": 2,
  "DUP_TOP": 1,
  "UNPACK_SEQUENCE": 1,
  "RETURN_VALUE": 1,
  "LIST_APPEND": lambda op: cast(int, op.arg) + 1, # arg captures the location of the list being built on the stack
}

# Opcodes to instrument after they run
post_opcode_instrument = {
  "LOAD_NAME": 1,
  "LOAD_FAST": 1,
  "LOAD_DEREF": 1,
  "LOAD_CLOSURE": 1,
  "LOAD_CONST": 1,
  "LOAD_GLOBAL": 1,
  "BUILD_LIST": 1,
  "BUILD_SLICE": 1,
  "BUILD_TUPLE": 1,
  "LOAD_METHOD": {False: 1, True: 2}, # capture method and self parameter
  "LOAD_ATTR": 1,
  "GET_ITER": 1, 
}

pre_and_post_opcode_instrument: Dict[str, Tuple[Union[int, Callable[[Instr], int], Dict[bool, Any]], Union[int, Callable[[Instr], int], Dict[bool, Any]]]] = {
  "FOR_ITER": (1,1),
  # "LOAD_ATTR": (1,1),
  "CALL_METHOD": ({False: lambda op: cast(int, op.arg) + 1, True: lambda op: cast(int, op.arg) + 2}, 1), 
  # capture all args as well as the function as well as self, then capture return value
  "CALL_FUNCTION_EX": (2, 1), # We only implement the case of variadic positional arguments only. Arguments bundled into one list
  "CALL_FUNCTION_KW": (lambda op: cast(int, op.arg) + 2, 1), # capture all args as well as the function as well as keys, then capture return value
  "CALL_FUNCTION": (lambda op: cast(int, op.arg) + 1, 1), # capture all args as well as the function, then capture return value
  "MAKE_FUNCTION": (lambda op: 2 if cast(int, op.arg) == 0 else 3, 1),
}

for op in binary_ops:
  pre_opcode_instrument[op] = 2
  post_opcode_instrument[op] = 1

for op in unary_ops:
  pre_opcode_instrument[op] = 1
  post_opcode_instrument[op] = 1

for op in pre_and_post_opcode_instrument:
  pre_opcode_instrument[op], post_opcode_instrument[op] = pre_and_post_opcode_instrument[op]

def emit_guarded_instrument(
  instrumented: Bytecode,
  op: Instr, i: int, guarded_stacksize: int, stacksize: Dict[bool, int],
  label_to_op_index: Dict[Label, int],
  code_id: int, is_post: bool,
  opcode: Optional[Union[int, Literal["JUMP_TARGET"]]] = None,
  arg: Any = None
) -> None:
  assert guarded_stacksize > 0, "No elements being inspected dynamically, guarded instrumentation should not be needed."
  
  def emit_unpack_args():
    instrumented.append(Instr(
      name = "LOAD_GLOBAL",
      arg = "reversed",
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "ROT_TWO",
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "CALL_FUNCTION",
      arg = 1,
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "UNPACK_SEQUENCE",
      arg = guarded_stacksize,
      lineno = op.lineno
    ))

  label_cond_to_else = Label()
  label_then_to_outside = Label()

  instrumented.append(Instr(
    name = "BUILD_LIST",
    arg = guarded_stacksize,
    lineno=op.lineno
  ))

  instrumented.append(Instr(
    name="DUP_TOP",
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_GLOBAL",
    arg = "dynamic_instrumentation_guide",
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "ROT_TWO"
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = opcode if opcode else op.opcode,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = is_post,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "CALL_FUNCTION",
    arg = 3,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "POP_JUMP_IF_TRUE",
    arg = label_cond_to_else,
    lineno = op.lineno
  ))

  emit_unpack_args()

  emit_instrument(instrumented, op, i, stacksize[False], label_to_op_index, code_id, is_post, opcode, arg)

  instrumented.append(Instr(
    name = "JUMP_ABSOLUTE",
    arg = label_then_to_outside,
    lineno = op.lineno
  ))

  instrumented.append(label_cond_to_else)

  emit_unpack_args()

  emit_instrument(instrumented, op, i, stacksize[True], label_to_op_index, code_id, is_post, opcode, arg)

  instrumented.append(label_then_to_outside)
  
def emit_instrument(
  instrumented: Bytecode,
  op: Instr, i: int, stacksize: int,
  label_to_op_index: Dict[Label, int],
  code_id: int, is_post: bool,
  opcode: Optional[Union[int, Literal["JUMP_TARGET"]]] = None,
  arg: Any = None
) -> None:
  def emit_kv(k: str, v: Union[str, int]) -> None:
    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = k,
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = v,
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "BUILD_MAP",
      arg = 1,
      lineno = op.lineno
    ))

  if stacksize > 0:
    instrumented.append(Instr(
      name = "BUILD_LIST",
      arg = stacksize,
      lineno = op.lineno
    ))

    # make a copy to send to the receiver
    instrumented.append(Instr(
      name = "DUP_TOP",
      lineno = op.lineno
    ))

  # load the receiver
  instrumented.append(Instr(
    name = "LOAD_GLOBAL",
    arg = "py_instrument_receiver",
    lineno = op.lineno
  ))

  if stacksize > 0:
    # move the list copy to the end of the stack
    instrumented.append(Instr(
      name = "ROT_TWO",
      lineno = op.lineno
    ))
  else:
    # add an empty list since we have zero stacksize
    instrumented.append(Instr(
      name = "BUILD_LIST",
      arg = 0,
      lineno = op.lineno
    ))

  # add additional parameters specifying the opcode, argument, and original op index
  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = opcode if opcode else op.opcode,
    lineno = op.lineno
  ))

  if not arg:
    arg = op.arg

  if isinstance(arg, Label):
    emit_kv("label", label_to_op_index[arg])
  elif isinstance(arg, CellVar):
    emit_kv("cell", arg.name)
  elif isinstance(arg, FreeVar):
    emit_kv("free", arg.name)
  else:
    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = None if arg == UNSET else arg,
      lineno = op.lineno
    ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = i,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = code_id,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = is_post,
    lineno = op.lineno
  ))

  # call the receiver
  instrumented.append(Instr(
    name = "CALL_FUNCTION",
    arg = 6, # number of arguments
    lineno = op.lineno
  ))

  # ignore the receiver result
  instrumented.append(Instr(
    name = "POP_TOP",
    lineno = op.lineno
  ))

  if stacksize > 0:
    if stacksize > 1:
      # reverse the stored stack since it is unpacked right-to-left
      instrumented.append(Instr(
        name = "LOAD_GLOBAL",
        arg = "reversed",
        lineno = op.lineno
      ))

      # move the argument after the callable
      instrumented.append(Instr(
        name = "ROT_TWO",
        lineno = op.lineno
      ))

      # call the function so that the only thing left on the stack by us is the reversed list
      instrumented.append(Instr(
        name = "CALL_FUNCTION",
        arg = 1,
        lineno = op.lineno
      ))

    # and unpack the list back onto the stack
    instrumented.append(Instr(
      name = "UNPACK_SEQUENCE",
      arg = stacksize,
      lineno = op.lineno
    ))

def run_or_return_value(maybe_lambda: Union[int, Callable[[Instr], int]], input: Instr) -> Union[int, Dict[bool, int]]:
  if callable(maybe_lambda):
    return maybe_lambda(input)
  elif isinstance(maybe_lambda, dict):
    concretized = {}
    for key, value in maybe_lambda.items():
      concretized[key] = run_or_return_value(value, input)
    return concretized
  else:
    return maybe_lambda

def instrument_bytecode(code: Bytecode, code_id: int = 0) -> Bytecode:
  instrumented = clone_bytecode_empty_body(code)

  label_to_op_index = {}
  for i in range(len(code)):
    if isinstance(code[i], Label):
      label_to_op_index[code[i]] = i + 1

  for i in range(len(code)):
    op = code[i]

    printDebug(op)

    if isinstance(op, Instr) and op.name in pre_opcode_instrument:
      if isinstance(pre_opcode_instrument[op.name], dict):
        concretized = run_or_return_value(pre_opcode_instrument[op.name], op)
        emit_guarded_instrument(
          instrumented, op, i, 
          min(concretized.values()), concretized,
          label_to_op_index, code_id, False
        )
        # emit_instrument(
        #   instrumented, op, i,
        #   run_or_return_value(pre_opcode_instrument[op.name][False], op),
        #   label_to_op_index, code_id, False
        # )
      else:
        emit_instrument(
          instrumented, op, i,
          run_or_return_value(pre_opcode_instrument[op.name], op),
          label_to_op_index, code_id, False
        )
    
    if isinstance(op, Instr) and op.name not in pre_opcode_instrument and op.name not in post_opcode_instrument:
      if op.name in ignore_ops:
        print(f"IGNORING OPERATION {op.name}")
      else:
        #if not op.name == "CALL_FUNCTION_EX" and not op.name == "IMPORT_FROM" and not op.name == "CALL_FUNCTION_KW" and not op.name == "RAISE_VARARGS":
        raise Exception(f"Unhandled Operation for Instrumentation: {op.name}")

    instrumented.append(op)

    if isinstance(op, Label):
      emit_instrument(
        instrumented, code[i + 1], i, 0, label_to_op_index, code_id, False,
        opcode="JUMP_TARGET", arg=op
      )

    if isinstance(op, Instr) and op.name in post_opcode_instrument:
      if isinstance(post_opcode_instrument[op.name], dict):
        concretized = run_or_return_value(post_opcode_instrument[op.name], op)
        emit_guarded_instrument(
          instrumented, op, i, 
          min(concretized.values()), concretized,
          label_to_op_index, code_id, True
        )
        # emit_instrument(
        #   instrumented, op, i,
        #   run_or_return_value(post_opcode_instrument[op.name][False], op),
        #   label_to_op_index, code_id, True
        # )
      else:
        emit_instrument(
          instrumented, op, i,
          run_or_return_value(post_opcode_instrument[op.name], op),
          label_to_op_index, code_id, True
        )
  
  return instrumented

def instrument_codeobject(code: CodeType, code_id: int = 0) -> Bytecode:
  return instrument_bytecode(Bytecode.from_code(code), code_id)

def instrument_source(source: str, code_id: int) -> Bytecode:
  return instrument_codeobject(compile(source, "<string>", "exec"), code_id)
