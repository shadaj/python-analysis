def testWildImpl():
  import Datasets.Wild.sum as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.prod as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.mean as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.max as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.min as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.all as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  a = np.asarray(a).astype(int).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func3(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.any as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  a = np.asarray(a).astype(int).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func2(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.count_nonzero as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.std as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func2(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.cumsum as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.argmax as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.argmin as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.add as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.where as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.choice([0,1], length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  c = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a, b, c)
  with receiver:
    ans = totest.func2(a, b, c)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.dot as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.matmul as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.outer as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.clip as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  lim1 = -3
  lim2 = 3
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a, lim1, lim2)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.diff as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.allclose as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, length).tolist()
  b = np.random.uniform(-10, 10, length).tolist()
  if np.random.choice([0,2]):
    b = a
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.transpose as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.ravel as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.reshape as totest
  import numpy as np
  length = np.random.randint(3,5)
  a = np.random.uniform(-10, 10, size=length**2).tolist()
  if length % 2:
    shp = (length, length)
  else:
    shp = (length * 2, length // 2) 
  print("inp: ", a, shp)
  with receiver:
    ans = totest.func1(a, shp)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.ravel as totest
  import numpy as np
  length = np.random.randint(3,5)
  a = np.random.uniform(-10, 10, size=(length,length)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.squeeze as totest
  import numpy as np
  length = np.random.randint(3,5)
  a = np.random.uniform(-10, 10, size=(1,length,1, length)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.atleast_1d as totest
  import numpy as np
  a = np.random.uniform(-10, 10, size=(1,)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.arange as totest
  import numpy as np
  
  with receiver:
    ans = totest.func1(15, 26, 2)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.concatenate as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  length = np.random.randint(3, 10)
  b = np.random.uniform(-10, 10, size=(length, length)).tolist()
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.vstack as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  b = np.random.uniform(-10, 10, size=(length, length)).tolist()
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.hstack as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  b = np.random.uniform(-10, 10, size=(length, length)).tolist()
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.tile as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  b = np.random.randint(2, 4)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.repeat as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  b = np.random.randint(2, 4)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.append as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length)).tolist()
  b = np.random.randint(2, 5)
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.insert as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length)).tolist()
  ind = np.random.randint(length)
  b = np.random.randint(2, 5)
  print("inp: ", a, b)
  with receiver:
    ans = totest.func1(a, ind, b)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.eye as totest
  import numpy as np
  n = np.random.randint(2, 4)
  print("inp: ", n)
  with receiver:
    ans = totest.func1(n)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.diag as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.uniform(-10, 10, size=(length, length)).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.full as totest
  import numpy as np
  length = np.random.randint(3, 5)
  a = np.random.randint(-5, 5)
  print("inp: ", a)
  with receiver:
    ans = totest.func1((length, length), a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.sort as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.random(size=length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.argsort as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.random(size=length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.percentile as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.random(size=length).tolist()
  p = 25
  print("inp: ", a, p)
  with receiver:
    ans = totest.func1(a, p)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.median as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.random(size=length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)

def testWildImpl():
  import Datasets.Wild.unique as totest
  import numpy as np
  length = np.random.randint(3, 10)
  a = np.random.randint(0, 10, size=length).tolist()
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)