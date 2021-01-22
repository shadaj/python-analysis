from instrumentation.instrument_nested import extract_all_codeobjects, instrument_extracted
from run_instrumented import run_with_handler
from .util import diff_bytecodes

from dis import opname
from textwrap import dedent

import re

def source_test(snapshot, source):
  root_codeobject = compile(source, "<string>", "exec")
  [id_to_bytecode, code_to_id] = extract_all_codeobjects(root_codeobject)
  id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

  code_id_to_mapping = {}
  diff_string = ""
  for code_id in id_to_bytecode.keys():
    diff_string += "\n"
    diff_string += "Code Object: " + id_to_bytecode[code_id].name + "\n"

    (cur_diff, cur_mapping) = diff_bytecodes(id_to_bytecode[code_id], id_to_bytecode_new_codeobjects[code_id])
    diff_string += cur_diff
    code_id_to_mapping[code_id] = cur_mapping

    diff_string += "\n"

  snapshot.assert_match(diff_string)

  def clean_stack_addresses(elem):
    if type(elem).__name__ == "cell": # CellType only in Python 3.8
      return re.sub(
        "0x[a-zA-Z0-9]+",
        "SOME ADDRESS",
        str(elem)
      )
    else:
      return elem

  events = []
  def event_receiver(stack, opcode, arg, opindex, code_id, is_post):
    if opcode == "JUMP_TARGET":
      events.append({ "arrive_at": code_id_to_mapping[code_id][arg["label"]] * 2 })
    else:
      events.append({
        "stack": list(map(clean_stack_addresses, stack)),
        "opcode": opcode if isinstance(opcode, str) else opname[opcode],
        "arg": { "label": code_id_to_mapping[code_id][arg["label"]] * 2 } if (isinstance(arg, dict) and "label" in arg) else arg,
        "orig_op": code_id_to_mapping[code_id][opindex] * 2,
        "code": id_to_bytecode[code_id].name,
        "is_post": is_post
      })

  run_with_handler(id_to_bytecode_new_codeobjects[code_to_id[root_codeobject]].to_code(), event_receiver)

  snapshot.assert_match(events)

def test_load_name(snapshot):
  source_test(snapshot, dedent(
    """
    list
    """
  ))

def test_store_name(snapshot):
  source_test(snapshot, dedent(
    """
    x = 1
    """
  ))

def test_load_attr(snapshot):
  source_test(snapshot, dedent(
    """
    x = range(0,5)
    x.start
    """
  ))

def test_store_attr(snapshot):
  source_test(snapshot, dedent(
    """
    x = type('', (), {})()
    x.a = 1
    """
  ))

def test_store_then_load(snapshot):
  source_test(snapshot, dedent(
    """
    x = 1
    x
    """
  ))

def test_list_load(snapshot):
  source_test(snapshot, dedent(
    """
    arr = [1, 2, 3]
    arr[1]
    """
  ))

def test_list_store(snapshot):
  source_test(snapshot, dedent(
    """
    arr = [1, 2, 3]
    arr[1] = 2
    """
  ))

def test_for_loop(snapshot):
  source_test(snapshot, dedent(
    """
    for i in [1, 2, 3]:
      pass
    """
  ))

def test_function_call(snapshot):
  source_test(snapshot, dedent(
    """
    def f():
      pass
    f()
    """
  ))

def test_function_call_with_args(snapshot):
  source_test(snapshot, dedent(
    """
    def f(x):
      return x
    f(1)
    """
  ))

def test_inner_function(snapshot):
  source_test(snapshot, dedent(
    """
    def f():
      def g():
        pass
      g()
    f()
    """
  ))

def test_inner_function_nonlocal_ref(snapshot):
  source_test(snapshot, dedent(
    """
    def f(i):
      def g():
        nonlocal i
        return i
      g()
    f(1)
    """
  ))
