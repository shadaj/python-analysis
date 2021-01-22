# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_load_name 1'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (xx)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('xx')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 POP_TOP
              28 LOAD_CONST               4 (None)
              30 RETURN_VALUE
'''

snapshots['test_store_name 1'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (90)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               0 (1)
+             16 LOAD_CONST               3 (0)
+             18 LOAD_CONST               4 (False)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 STORE_NAME               1 (x)
              28 LOAD_CONST               5 (None)
              30 RETURN_VALUE
'''

snapshots['test_load_attr 1'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('x')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               4 (106)
+             36 LOAD_CONST               5 ('a')
+             38 LOAD_CONST               6 (1)
+             40 LOAD_CONST               2 (0)
+             42 LOAD_CONST               7 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 LOAD_ATTR                2 (a)
+             52 BUILD_LIST               1
+             54 DUP_TOP
+             56 LOAD_GLOBAL              1 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               4 (106)
+             62 LOAD_CONST               5 ('a')
+             64 LOAD_CONST               6 (1)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               3 (True)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 UNPACK_SEQUENCE          1
              76 POP_TOP
              78 LOAD_CONST               8 (None)
              80 RETURN_VALUE
'''

snapshots['test_store_attr 1'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
               2 LOAD_NAME                0 (x)
+              4 BUILD_LIST               1
+              6 DUP_TOP
+              8 LOAD_GLOBAL              1 (py_instrument_receiver)
+             10 ROT_TWO
+             12 LOAD_CONST               1 (101)
+             14 LOAD_CONST               2 ('x')
+             16 LOAD_CONST               0 (1)
+             18 LOAD_CONST               3 (0)
+             20 LOAD_CONST               4 (True)
+             22 CALL_FUNCTION            6
+             24 POP_TOP
+             26 UNPACK_SEQUENCE          1
+             28 BUILD_LIST               2
+             30 DUP_TOP
+             32 LOAD_GLOBAL              1 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               5 (95)
+             38 LOAD_CONST               6 ('a')
+             40 LOAD_CONST               7 (2)
+             42 LOAD_CONST               3 (0)
+             44 LOAD_CONST               8 (False)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 LOAD_GLOBAL              2 (reversed)
+             52 ROT_TWO
+             54 CALL_FUNCTION            1
+             56 UNPACK_SEQUENCE          2
              58 STORE_ATTR               3 (a)
              60 LOAD_CONST               9 (None)
              62 RETURN_VALUE
'''

snapshots['test_list_load 1'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('x')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 (1)
+             28 BUILD_LIST               2
+             30 DUP_TOP
+             32 LOAD_GLOBAL              1 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               5 (25)
+             38 LOAD_CONST               6 (None)
+             40 LOAD_CONST               7 (2)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               8 (False)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 LOAD_GLOBAL              2 (reversed)
+             52 ROT_TWO
+             54 CALL_FUNCTION            1
+             56 UNPACK_SEQUENCE          2
              58 BINARY_SUBSCR
+             60 BUILD_LIST               1
+             62 DUP_TOP
+             64 LOAD_GLOBAL              1 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST               5 (25)
+             70 LOAD_CONST               6 (None)
+             72 LOAD_CONST               7 (2)
+             74 LOAD_CONST               2 (0)
+             76 LOAD_CONST               3 (True)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 UNPACK_SEQUENCE          1
              84 POP_TOP
              86 LOAD_CONST               6 (None)
              88 RETURN_VALUE
'''

snapshots['test_list_store 1'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
               2 LOAD_NAME                0 (x)
+              4 BUILD_LIST               1
+              6 DUP_TOP
+              8 LOAD_GLOBAL              1 (py_instrument_receiver)
+             10 ROT_TWO
+             12 LOAD_CONST               1 (101)
+             14 LOAD_CONST               2 ('x')
+             16 LOAD_CONST               0 (1)
+             18 LOAD_CONST               3 (0)
+             20 LOAD_CONST               4 (True)
+             22 CALL_FUNCTION            6
+             24 POP_TOP
+             26 UNPACK_SEQUENCE          1
              28 LOAD_CONST               0 (1)
+             30 BUILD_LIST               3
+             32 DUP_TOP
+             34 LOAD_GLOBAL              1 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               5 (60)
+             40 LOAD_CONST               6 (None)
+             42 LOAD_CONST               7 (3)
+             44 LOAD_CONST               3 (0)
+             46 LOAD_CONST               8 (False)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 LOAD_GLOBAL              2 (reversed)
+             54 ROT_TWO
+             56 CALL_FUNCTION            1
+             58 UNPACK_SEQUENCE          3
              60 STORE_SUBSCR
              62 LOAD_CONST               6 (None)
              64 RETURN_VALUE
'''

snapshots['test_for_loop 1'] = '''
Code Object: <module>
+  2           0 LOAD_GLOBAL              0 (py_instrument_receiver)
+              2 BUILD_LIST               0
+              4 LOAD_CONST               0 (120)
+              6 LOAD_CONST               1 ('label')
+              8 LOAD_CONST               2 (10)
+             10 BUILD_MAP                1
+             12 LOAD_CONST               3 (0)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (False)
+             18 CALL_FUNCTION            6
+             20 POP_TOP
              22 SETUP_LOOP              80 (to 104)
              24 LOAD_CONST               5 (None)
              26 GET_ITER
+        >>   28 LOAD_GLOBAL              0 (py_instrument_receiver)
+             30 BUILD_LIST               0
+             32 LOAD_CONST               6 ('JUMP_TARGET')
+             34 LOAD_CONST               1 ('label')
+             36 LOAD_CONST               7 (4)
+             38 BUILD_MAP                1
+             40 LOAD_CONST               8 (3)
+             42 LOAD_CONST               3 (0)
+             44 LOAD_CONST               4 (False)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
              50 FOR_ITER                28 (to 80)
+             52 BUILD_LIST               1
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               9 (90)
+             62 LOAD_CONST              10 ('i')
+             64 LOAD_CONST              11 (5)
+             66 LOAD_CONST               3 (0)
+             68 LOAD_CONST               4 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 UNPACK_SEQUENCE          1
              76 STORE_NAME               1 (i)
   3          78 JUMP_ABSOLUTE           28
+        >>   80 LOAD_GLOBAL              0 (py_instrument_receiver)
+             82 BUILD_LIST               0
+             84 LOAD_CONST               6 ('JUMP_TARGET')
+             86 LOAD_CONST               1 ('label')
+             88 LOAD_CONST              12 (8)
+             90 BUILD_MAP                1
+             92 LOAD_CONST              13 (7)
+             94 LOAD_CONST               3 (0)
+             96 LOAD_CONST               4 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
             102 POP_BLOCK
+        >>  104 LOAD_GLOBAL              0 (py_instrument_receiver)
+            106 BUILD_LIST               0
+            108 LOAD_CONST               6 ('JUMP_TARGET')
+            110 LOAD_CONST               1 ('label')
+            112 LOAD_CONST               2 (10)
+            114 BUILD_MAP                1
+            116 LOAD_CONST              14 (9)
+            118 LOAD_CONST               3 (0)
+            120 LOAD_CONST               4 (False)
+            122 CALL_FUNCTION            6
+            124 POP_TOP
             126 LOAD_CONST               5 (None)
             128 RETURN_VALUE
'''

snapshots['test_while_loop 1'] = '''
Code Object: <module>
+  2           0 LOAD_GLOBAL              0 (py_instrument_receiver)
+              2 BUILD_LIST               0
+              4 LOAD_CONST               0 (120)
+              6 LOAD_CONST               1 ('label')
+              8 LOAD_CONST               2 (5)
+             10 BUILD_MAP                1
+             12 LOAD_CONST               3 (0)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (False)
+             18 CALL_FUNCTION            6
+             20 POP_TOP
              22 SETUP_LOOP              26 (to 50)
+  3     >>   24 LOAD_GLOBAL              0 (py_instrument_receiver)
+             26 BUILD_LIST               0
+             28 LOAD_CONST               5 ('JUMP_TARGET')
+             30 LOAD_CONST               1 ('label')
+             32 LOAD_CONST               6 (2)
+             34 BUILD_MAP                1
+             36 LOAD_CONST               7 (1)
+             38 LOAD_CONST               3 (0)
+             40 LOAD_CONST               4 (False)
+             42 CALL_FUNCTION            6
+             44 POP_TOP
              46 JUMP_ABSOLUTE           24
              48 POP_BLOCK
+        >>   50 LOAD_GLOBAL              0 (py_instrument_receiver)
+             52 BUILD_LIST               0
+             54 LOAD_CONST               5 ('JUMP_TARGET')
+             56 LOAD_CONST               1 ('label')
+             58 LOAD_CONST               2 (5)
+             60 BUILD_MAP                1
+             62 LOAD_CONST               8 (4)
+             64 LOAD_CONST               3 (0)
+             66 LOAD_CONST               4 (False)
+             68 CALL_FUNCTION            6
+             70 POP_TOP
              72 LOAD_CONST               9 (None)
              74 RETURN_VALUE
'''

snapshots['test_function_definition 1'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
               2 LOAD_CONST               1 ('f')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (90)
+             16 LOAD_CONST               1 ('f')
+             18 LOAD_CONST               3 (3)
+             20 LOAD_CONST               4 (0)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_NAME               1 (f)
   4          32 LOAD_NAME                1 (f)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (101)
+             44 LOAD_CONST               1 ('f')
+             46 LOAD_CONST               7 (4)
+             48 LOAD_CONST               4 (0)
+             50 LOAD_CONST               8 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               9 (131)
+             68 LOAD_CONST               4 (0)
+             70 LOAD_CONST              10 (5)
+             72 LOAD_CONST               4 (0)
+             74 LOAD_CONST               5 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 CALL_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               9 (131)
+             94 LOAD_CONST               4 (0)
+             96 LOAD_CONST              10 (5)
+             98 LOAD_CONST               4 (0)
+            100 LOAD_CONST               8 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
             108 POP_TOP
             110 LOAD_CONST              11 (None)
             112 RETURN_VALUE

Code Object: f
   3           0 LOAD_CONST               0 (None)
               2 RETURN_VALUE
'''

snapshots['test_inner_function 1'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
               2 LOAD_CONST               1 ('f')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (90)
+             16 LOAD_CONST               1 ('f')
+             18 LOAD_CONST               3 (3)
+             20 LOAD_CONST               4 (0)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_NAME               1 (f)
   6          32 LOAD_NAME                1 (f)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (101)
+             44 LOAD_CONST               1 ('f')
+             46 LOAD_CONST               7 (4)
+             48 LOAD_CONST               4 (0)
+             50 LOAD_CONST               8 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               9 (131)
+             68 LOAD_CONST               4 (0)
+             70 LOAD_CONST              10 (5)
+             72 LOAD_CONST               4 (0)
+             74 LOAD_CONST               5 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 CALL_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               9 (131)
+             94 LOAD_CONST               4 (0)
+             96 LOAD_CONST              10 (5)
+             98 LOAD_CONST               4 (0)
+            100 LOAD_CONST               8 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
             108 POP_TOP
             110 LOAD_CONST              11 (None)
             112 RETURN_VALUE

Code Object: f
~  3           0 LOAD_CONST               0 (<code object g at SOME ADDRESS, file "<string>", line 3>)
               2 LOAD_CONST               1 ('f.<locals>.g')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (125)
+             16 LOAD_CONST               3 ('g')
+             18 LOAD_CONST               4 (3)
+             20 LOAD_CONST               5 (1)
+             22 LOAD_CONST               6 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_FAST               0 (g)
   5          32 LOAD_FAST                0 (g)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               7 (124)
+             44 LOAD_CONST               3 ('g')
+             46 LOAD_CONST               8 (4)
+             48 LOAD_CONST               5 (1)
+             50 LOAD_CONST               9 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST              10 (131)
+             68 LOAD_CONST              11 (0)
+             70 LOAD_CONST              12 (5)
+             72 LOAD_CONST               5 (1)
+             74 LOAD_CONST               6 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 CALL_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST              10 (131)
+             94 LOAD_CONST              11 (0)
+             96 LOAD_CONST              12 (5)
+             98 LOAD_CONST               5 (1)
+            100 LOAD_CONST               9 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
             108 POP_TOP
             110 LOAD_CONST              13 (None)
             112 RETURN_VALUE

Code Object: g
   4           0 LOAD_CONST               0 (None)
               2 RETURN_VALUE
'''

snapshots['test_nonlocal_ref 1'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
               2 LOAD_CONST               1 ('f')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (90)
+             16 LOAD_CONST               1 ('f')
+             18 LOAD_CONST               3 (3)
+             20 LOAD_CONST               4 (0)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_NAME               1 (f)
   8          32 LOAD_NAME                1 (f)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (101)
+             44 LOAD_CONST               1 ('f')
+             46 LOAD_CONST               7 (4)
+             48 LOAD_CONST               4 (0)
+             50 LOAD_CONST               8 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               9 (131)
+             68 LOAD_CONST               4 (0)
+             70 LOAD_CONST              10 (5)
+             72 LOAD_CONST               4 (0)
+             74 LOAD_CONST               5 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 CALL_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               9 (131)
+             94 LOAD_CONST               4 (0)
+             96 LOAD_CONST              10 (5)
+             98 LOAD_CONST               4 (0)
+            100 LOAD_CONST               8 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
             108 POP_TOP
             110 LOAD_CONST              11 (None)
             112 RETURN_VALUE

Code Object: f
   3           0 LOAD_CONST               0 (0)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (137)
+             12 LOAD_CONST               2 ('cell')
+             14 LOAD_CONST               3 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               4 (1)
+             20 LOAD_CONST               4 (1)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_DEREF              0 (i)
   4          32 LOAD_CLOSURE             0 (i)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (135)
+             44 LOAD_CONST               2 ('cell')
+             46 LOAD_CONST               3 ('i')
+             48 BUILD_MAP                1
+             50 LOAD_CONST               7 (2)
+             52 LOAD_CONST               4 (1)
+             54 LOAD_CONST               8 (True)
+             56 CALL_FUNCTION            6
+             58 POP_TOP
+             60 UNPACK_SEQUENCE          1
              62 BUILD_TUPLE              1
~             64 LOAD_CONST               9 (<code object g at SOME ADDRESS, file "<string>", line 4>)
              66 LOAD_CONST              10 ('f.<locals>.g')
              68 MAKE_FUNCTION            8
+             70 BUILD_LIST               1
+             72 DUP_TOP
+             74 LOAD_GLOBAL              0 (py_instrument_receiver)
+             76 ROT_TWO
+             78 LOAD_CONST              11 (125)
+             80 LOAD_CONST              12 ('g')
+             82 LOAD_CONST              13 (7)
+             84 LOAD_CONST               4 (1)
+             86 LOAD_CONST               5 (False)
+             88 CALL_FUNCTION            6
+             90 POP_TOP
+             92 UNPACK_SEQUENCE          1
              94 STORE_FAST               0 (g)
   7          96 LOAD_FAST                0 (g)
+             98 BUILD_LIST               1
+            100 DUP_TOP
+            102 LOAD_GLOBAL              0 (py_instrument_receiver)
+            104 ROT_TWO
+            106 LOAD_CONST              14 (124)
+            108 LOAD_CONST              12 ('g')
+            110 LOAD_CONST              15 (8)
+            112 LOAD_CONST               4 (1)
+            114 LOAD_CONST               8 (True)
+            116 CALL_FUNCTION            6
+            118 POP_TOP
+            120 UNPACK_SEQUENCE          1
+            122 BUILD_LIST               1
+            124 DUP_TOP
+            126 LOAD_GLOBAL              0 (py_instrument_receiver)
+            128 ROT_TWO
+            130 LOAD_CONST              16 (131)
+            132 LOAD_CONST               0 (0)
+            134 LOAD_CONST              17 (9)
+            136 LOAD_CONST               4 (1)
+            138 LOAD_CONST               5 (False)
+            140 CALL_FUNCTION            6
+            142 POP_TOP
+            144 UNPACK_SEQUENCE          1
             146 CALL_FUNCTION            0
+            148 BUILD_LIST               1
+            150 DUP_TOP
+            152 LOAD_GLOBAL              0 (py_instrument_receiver)
+            154 ROT_TWO
+            156 LOAD_CONST              16 (131)
+            158 LOAD_CONST               0 (0)
+            160 LOAD_CONST              17 (9)
+            162 LOAD_CONST               4 (1)
+            164 LOAD_CONST               8 (True)
+            166 CALL_FUNCTION            6
+            168 POP_TOP
+            170 UNPACK_SEQUENCE          1
             172 POP_TOP
             174 LOAD_CONST              18 (None)
             176 RETURN_VALUE

Code Object: g
   6           0 LOAD_DEREF               0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (136)
+             12 LOAD_CONST               1 ('free')
+             14 LOAD_CONST               2 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               3 (0)
+             20 LOAD_CONST               4 (2)
+             22 LOAD_CONST               5 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 RETURN_VALUE
'''
