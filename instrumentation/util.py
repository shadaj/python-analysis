from bytecode import Bytecode, Instr
from types import CodeType

def clone_bytecode_empty_body(code):
  instrumented = Bytecode()
  instrumented.first_lineno = code.first_lineno
  instrumented.name = code.name
  instrumented.filename = code.filename
  
  instrumented.argcount = code.argcount
  instrumented.argnames = code.argnames
  instrumented.cellvars = code.cellvars
  instrumented.freevars = code.freevars
  
  return instrumented

def is_const_load_function(instr):
  return isinstance(instr, Instr) and instr.name == "LOAD_CONST" and isinstance(instr.arg, CodeType)
