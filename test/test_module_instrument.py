import sys

from dis import opname

from instrumentation.module_loader import PatchingPathFinder, add_receiver
from .test_core_constructs_exec import clean_stack_addresses

def logging_receiver():
  log = []
  def receiver(stack, opcode, arg, opindex, code_id, is_post, id_to_orig_bytecode):
    print(opcode)
    if opcode == "JUMP_TARGET":
      log.append({ "arrive_at": arg["label"] })
    else:
      log.append({
        "stack": list(map(clean_stack_addresses, stack)),
        "opcode": opcode if isinstance(opcode, str) else opname[opcode],
        "arg": arg,
        "is_post": is_post
      })
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
  del sys.modules["test.simple_module_to_import"]
