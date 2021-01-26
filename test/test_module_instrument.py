import re
from types import ModuleType

from dis import opname

from instrumentation.module_loader import PatchingPathFinder, add_receiver

def cleanup_elem(e):
  if isinstance(e, ModuleType):
    return "<module " + e.__name__ + ">"
  else:
    return re.sub(
      "0x[a-zA-Z0-9]+",
      "SOME ADDRESS",
      str(e)
    )

def logging_receiver():
  log = []
  is_in_receiver = False
  def receiver(stack, opcode, arg, opindex, code_id, is_post, id_to_orig_bytecode):
    nonlocal is_in_receiver
    if is_in_receiver:
      return # stringifying can result in recursion
    is_in_receiver = True
    if opcode == "JUMP_TARGET":
      log.append({ "arrive_at": arg["label"] })
    else:
      log.append({
        "stack": list(map(cleanup_elem, stack)),
        "opcode": opcode if isinstance(opcode, str) else opname[opcode],
        "arg": arg,
        "is_post": is_post
      })
    is_in_receiver = False

  return receiver, log

def test_calls_to_module_function(snapshot):
  patcher = PatchingPathFinder()
  patcher.install()
  receiver, log = logging_receiver()
  remove_receiver = add_receiver(receiver)

  from .simple_module_to_import import hello
  hello()

  snapshot.assert_match(log)
  remove_receiver()
  patcher.uninstall()

def test_calls_to_numpy_function(snapshot):
  patcher = PatchingPathFinder()
  patcher.install()

  import numpy as np

  receiver, log = logging_receiver()
  remove_receiver = add_receiver(receiver)

  np.linalg.eigvals(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

  snapshot.assert_match(log)
  remove_receiver()
  patcher.uninstall()
