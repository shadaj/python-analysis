#!/usr/bin/env python3
from bytecode import Bytecode, dump_bytecode
from textwrap import dedent

from test.util import diff_bytecodes

from instrumentation.stack_tracking_receiver import StackTrackingReceiver

from instrumentation.instrument_nested import extract_all_codeobjects, instrument_extracted

def run_with_handler(code, handler):
  exec(code, {
    "py_instrument_receiver": handler
  })

def instrument_and_exec(source):
  root_codeobject = compile(source, "<string>", "exec")
  [id_to_bytecode, code_to_id] = extract_all_codeobjects(root_codeobject)
  id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

  instrumented = id_to_bytecode_new_codeobjects[code_to_id[root_codeobject]]
  orig_bytecode = Bytecode.from_code(compile(source, "<string>", "exec"))

  for code_id in id_to_bytecode.keys():
    print(id_to_bytecode[code_id].name)
    print(diff_bytecodes(id_to_bytecode[code_id], id_to_bytecode_new_codeobjects[code_id])[0])

  print()

  print("For label reference:")
  for orig_bytecode in id_to_bytecode.values():
    dump_bytecode(orig_bytecode, lineno=True)

  run_with_handler(instrumented.to_code(), StackTrackingReceiver(id_to_bytecode))

if __name__ == '__main__':
  # source = dedent(
    # """
    # def myFunc():
    #   x = -1
    #   data = list(range(5))
    #   for i in data:
    #     if i == 3:
    #       break
    #     else:
    #       while i > 0:
    #         x += i
    #         i -= 1
    # myFunc()
    # """
  # )

  # source = dedent(
    # """
    # def factorial(i):
    #   if i == 0:
    #     return 1
    #   else:
    #     return i * factorial(i - 1)

    # factorial(5)
    # """
  # )

  # source = dedent(
    # """
    # my_arr = [1, 2, 3]
    # for i in range(0, 3):
    #   my_arr[i] = my_arr[i] + 1
    # """
  # )

  source = dedent(
    """
    x = 1
    y = 2
    z = 3

    
    def f1():
        print(x)
        w = 4
        u = 5
    
        def f2():
            print(x)
            u = 6
            print(u)
            print(w)
    
            def f3():
                print(u)
                print(w)
                print(x)
    
            f3()
        f2()

    f1()
    """
  )

  instrument_and_exec(source)
