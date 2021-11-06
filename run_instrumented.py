from textwrap import dedent

from instrumentation.stack_tracking_receiver import StackTrackingReceiver
from instrumentation.module_loader import PatchingPathFinder
from instrumentation.exec import exec_instrumented

patcher = PatchingPathFinder()
patcher.install()

from demos.quicksort import quick1

import random
arr = [random.randint(0, 10) for i in range(2)]
print(arr)
receiver = StackTrackingReceiver()
with receiver:
  quick1(arr)
print(arr)
print([receiver.stringify_maybe_object_id(x.concrete) for x in receiver.symbolic_stack])

# import numpy as np
# arr = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# with StackTrackingReceiver():
#   np.linalg.eigvals(arr)

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

# source = dedent(
#   """
#   x = 1 # global so won't show up in trace because we don't instrument globals yet
#   y = 2
#   z = 3


#   def f1():
#       print(x)
#       w = 4
#       u = 5

#       def f2():
#           print(x)
#           u = 6
#           print(u)
#           print(w)

#           def f3():
#               print(u)
#               print(w)
#               print(x)

#           f3()
#       f2()

#   f1()
#   """
# )

# with StackTrackingReceiver():
#   exec_instrumented(source)
