# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_load_name (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (list)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('list')
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

snapshots['test_store_name (1, 3, 7)'] = '''
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

snapshots['test_load_attr (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (range)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('range')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               2 (0)
              28 LOAD_CONST               4 (5)
+             30 BUILD_LIST               3
+             32 DUP_TOP
+             34 LOAD_GLOBAL              1 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               5 (131)
+             40 LOAD_CONST               6 (2)
+             42 LOAD_CONST               7 (3)
+             44 LOAD_CONST               2 (0)
+             46 LOAD_CONST               8 (False)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 LOAD_GLOBAL              2 (reversed)
+             54 ROT_TWO
+             56 CALL_FUNCTION            1
+             58 UNPACK_SEQUENCE          3
              60 CALL_FUNCTION            2
+             62 BUILD_LIST               1
+             64 DUP_TOP
+             66 LOAD_GLOBAL              1 (py_instrument_receiver)
+             68 ROT_TWO
+             70 LOAD_CONST               5 (131)
+             72 LOAD_CONST               6 (2)
+             74 LOAD_CONST               7 (3)
+             76 LOAD_CONST               2 (0)
+             78 LOAD_CONST               3 (True)
+             80 CALL_FUNCTION            6
+             82 POP_TOP
+             84 UNPACK_SEQUENCE          1
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              1 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST               9 (90)
+             96 LOAD_CONST              10 ('x')
+             98 LOAD_CONST              11 (4)
+            100 LOAD_CONST               2 (0)
+            102 LOAD_CONST               8 (False)
+            104 CALL_FUNCTION            6
+            106 POP_TOP
+            108 UNPACK_SEQUENCE          1
             110 STORE_NAME               3 (x)
   3         112 LOAD_NAME                3 (x)
+            114 BUILD_LIST               1
+            116 DUP_TOP
+            118 LOAD_GLOBAL              1 (py_instrument_receiver)
+            120 ROT_TWO
+            122 LOAD_CONST               0 (101)
+            124 LOAD_CONST              10 ('x')
+            126 LOAD_CONST               4 (5)
+            128 LOAD_CONST               2 (0)
+            130 LOAD_CONST               3 (True)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
+            138 BUILD_LIST               1
+            140 DUP_TOP
+            142 LOAD_GLOBAL              1 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST              12 (106)
+            148 LOAD_CONST              13 ('start')
+            150 LOAD_CONST              14 (6)
+            152 LOAD_CONST               2 (0)
+            154 LOAD_CONST               8 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 UNPACK_SEQUENCE          1
             162 LOAD_ATTR                4 (start)
+            164 BUILD_LIST               1
+            166 DUP_TOP
+            168 LOAD_GLOBAL              1 (py_instrument_receiver)
+            170 ROT_TWO
+            172 LOAD_CONST              12 (106)
+            174 LOAD_CONST              13 ('start')
+            176 LOAD_CONST              14 (6)
+            178 LOAD_CONST               2 (0)
+            180 LOAD_CONST               3 (True)
+            182 CALL_FUNCTION            6
+            184 POP_TOP
+            186 UNPACK_SEQUENCE          1
             188 POP_TOP
             190 LOAD_CONST              15 (None)
             192 RETURN_VALUE
'''

snapshots['test_store_attr (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (type)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('type')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('')
              28 LOAD_CONST               5 (())
              30 BUILD_MAP                0
+             32 BUILD_LIST               4
+             34 DUP_TOP
+             36 LOAD_GLOBAL              1 (py_instrument_receiver)
+             38 ROT_TWO
+             40 LOAD_CONST               6 (131)
+             42 LOAD_CONST               7 (3)
+             44 LOAD_CONST               8 (4)
+             46 LOAD_CONST               2 (0)
+             48 LOAD_CONST               9 (False)
+             50 CALL_FUNCTION            6
+             52 POP_TOP
+             54 LOAD_GLOBAL              2 (reversed)
+             56 ROT_TWO
+             58 CALL_FUNCTION            1
+             60 UNPACK_SEQUENCE          4
              62 CALL_FUNCTION            3
+             64 BUILD_LIST               1
+             66 DUP_TOP
+             68 LOAD_GLOBAL              1 (py_instrument_receiver)
+             70 ROT_TWO
+             72 LOAD_CONST               6 (131)
+             74 LOAD_CONST               7 (3)
+             76 LOAD_CONST               8 (4)
+             78 LOAD_CONST               2 (0)
+             80 LOAD_CONST               3 (True)
+             82 CALL_FUNCTION            6
+             84 POP_TOP
+             86 UNPACK_SEQUENCE          1
+             88 BUILD_LIST               1
+             90 DUP_TOP
+             92 LOAD_GLOBAL              1 (py_instrument_receiver)
+             94 ROT_TWO
+             96 LOAD_CONST               6 (131)
+             98 LOAD_CONST               2 (0)
+            100 LOAD_CONST              10 (5)
+            102 LOAD_CONST               2 (0)
+            104 LOAD_CONST               9 (False)
+            106 CALL_FUNCTION            6
+            108 POP_TOP
+            110 UNPACK_SEQUENCE          1
             112 CALL_FUNCTION            0
+            114 BUILD_LIST               1
+            116 DUP_TOP
+            118 LOAD_GLOBAL              1 (py_instrument_receiver)
+            120 ROT_TWO
+            122 LOAD_CONST               6 (131)
+            124 LOAD_CONST               2 (0)
+            126 LOAD_CONST              10 (5)
+            128 LOAD_CONST               2 (0)
+            130 LOAD_CONST               3 (True)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
+            138 BUILD_LIST               1
+            140 DUP_TOP
+            142 LOAD_GLOBAL              1 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST              11 (90)
+            148 LOAD_CONST              12 ('x')
+            150 LOAD_CONST              13 (6)
+            152 LOAD_CONST               2 (0)
+            154 LOAD_CONST               9 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 UNPACK_SEQUENCE          1
             162 STORE_NAME               3 (x)
   3         164 LOAD_CONST              14 (1)
             166 LOAD_NAME                3 (x)
+            168 BUILD_LIST               1
+            170 DUP_TOP
+            172 LOAD_GLOBAL              1 (py_instrument_receiver)
+            174 ROT_TWO
+            176 LOAD_CONST               0 (101)
+            178 LOAD_CONST              12 ('x')
+            180 LOAD_CONST              15 (8)
+            182 LOAD_CONST               2 (0)
+            184 LOAD_CONST               3 (True)
+            186 CALL_FUNCTION            6
+            188 POP_TOP
+            190 UNPACK_SEQUENCE          1
+            192 BUILD_LIST               2
+            194 DUP_TOP
+            196 LOAD_GLOBAL              1 (py_instrument_receiver)
+            198 ROT_TWO
+            200 LOAD_CONST              16 (95)
+            202 LOAD_CONST              17 ('a')
+            204 LOAD_CONST              18 (9)
+            206 LOAD_CONST               2 (0)
+            208 LOAD_CONST               9 (False)
+            210 CALL_FUNCTION            6
+            212 POP_TOP
+            214 LOAD_GLOBAL              2 (reversed)
+            216 ROT_TWO
+            218 CALL_FUNCTION            1
+            220 UNPACK_SEQUENCE          2
             222 STORE_ATTR               4 (a)
             224 LOAD_CONST              19 (None)
             226 RETURN_VALUE
'''

snapshots['test_store_then_load (1, 3, 7)'] = '''
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
   3          28 LOAD_NAME                1 (x)
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              0 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               5 (101)
+             40 LOAD_CONST               2 ('x')
+             42 LOAD_CONST               6 (2)
+             44 LOAD_CONST               3 (0)
+             46 LOAD_CONST               7 (True)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 UNPACK_SEQUENCE          1
              54 POP_TOP
              56 LOAD_CONST               8 (None)
              58 RETURN_VALUE
'''

snapshots['test_list_load (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
               2 LOAD_CONST               1 (2)
               4 LOAD_CONST               2 (3)
               6 BUILD_LIST               3
+              8 BUILD_LIST               1
+             10 DUP_TOP
+             12 LOAD_GLOBAL              0 (py_instrument_receiver)
+             14 ROT_TWO
+             16 LOAD_CONST               3 (90)
+             18 LOAD_CONST               4 ('arr')
+             20 LOAD_CONST               5 (4)
+             22 LOAD_CONST               6 (0)
+             24 LOAD_CONST               7 (False)
+             26 CALL_FUNCTION            6
+             28 POP_TOP
+             30 UNPACK_SEQUENCE          1
              32 STORE_NAME               1 (arr)
   3          34 LOAD_NAME                1 (arr)
+             36 BUILD_LIST               1
+             38 DUP_TOP
+             40 LOAD_GLOBAL              0 (py_instrument_receiver)
+             42 ROT_TWO
+             44 LOAD_CONST               8 (101)
+             46 LOAD_CONST               4 ('arr')
+             48 LOAD_CONST               9 (5)
+             50 LOAD_CONST               6 (0)
+             52 LOAD_CONST              10 (True)
+             54 CALL_FUNCTION            6
+             56 POP_TOP
+             58 UNPACK_SEQUENCE          1
              60 LOAD_CONST               0 (1)
+             62 BUILD_LIST               2
+             64 DUP_TOP
+             66 LOAD_GLOBAL              0 (py_instrument_receiver)
+             68 ROT_TWO
+             70 LOAD_CONST              11 (25)
+             72 LOAD_CONST              12 (None)
+             74 LOAD_CONST              13 (7)
+             76 LOAD_CONST               6 (0)
+             78 LOAD_CONST               7 (False)
+             80 CALL_FUNCTION            6
+             82 POP_TOP
+             84 LOAD_GLOBAL              2 (reversed)
+             86 ROT_TWO
+             88 CALL_FUNCTION            1
+             90 UNPACK_SEQUENCE          2
              92 BINARY_SUBSCR
+             94 BUILD_LIST               1
+             96 DUP_TOP
+             98 LOAD_GLOBAL              0 (py_instrument_receiver)
+            100 ROT_TWO
+            102 LOAD_CONST              11 (25)
+            104 LOAD_CONST              12 (None)
+            106 LOAD_CONST              13 (7)
+            108 LOAD_CONST               6 (0)
+            110 LOAD_CONST              10 (True)
+            112 CALL_FUNCTION            6
+            114 POP_TOP
+            116 UNPACK_SEQUENCE          1
             118 POP_TOP
             120 LOAD_CONST              12 (None)
             122 RETURN_VALUE
'''

snapshots['test_list_store (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
               2 LOAD_CONST               1 (2)
               4 LOAD_CONST               2 (3)
               6 BUILD_LIST               3
+              8 BUILD_LIST               1
+             10 DUP_TOP
+             12 LOAD_GLOBAL              0 (py_instrument_receiver)
+             14 ROT_TWO
+             16 LOAD_CONST               3 (90)
+             18 LOAD_CONST               4 ('arr')
+             20 LOAD_CONST               5 (4)
+             22 LOAD_CONST               6 (0)
+             24 LOAD_CONST               7 (False)
+             26 CALL_FUNCTION            6
+             28 POP_TOP
+             30 UNPACK_SEQUENCE          1
              32 STORE_NAME               1 (arr)
   3          34 LOAD_CONST               1 (2)
              36 LOAD_NAME                1 (arr)
+             38 BUILD_LIST               1
+             40 DUP_TOP
+             42 LOAD_GLOBAL              0 (py_instrument_receiver)
+             44 ROT_TWO
+             46 LOAD_CONST               8 (101)
+             48 LOAD_CONST               4 ('arr')
+             50 LOAD_CONST               9 (6)
+             52 LOAD_CONST               6 (0)
+             54 LOAD_CONST              10 (True)
+             56 CALL_FUNCTION            6
+             58 POP_TOP
+             60 UNPACK_SEQUENCE          1
              62 LOAD_CONST               0 (1)
+             64 BUILD_LIST               3
+             66 DUP_TOP
+             68 LOAD_GLOBAL              0 (py_instrument_receiver)
+             70 ROT_TWO
+             72 LOAD_CONST              11 (60)
+             74 LOAD_CONST              12 (None)
+             76 LOAD_CONST              13 (8)
+             78 LOAD_CONST               6 (0)
+             80 LOAD_CONST               7 (False)
+             82 CALL_FUNCTION            6
+             84 POP_TOP
+             86 LOAD_GLOBAL              2 (reversed)
+             88 ROT_TWO
+             90 CALL_FUNCTION            1
+             92 UNPACK_SEQUENCE          3
              94 STORE_SUBSCR
              96 LOAD_CONST              12 (None)
              98 RETURN_VALUE
'''

snapshots['test_for_loop (1, 3, 7)'] = '''
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
              24 LOAD_CONST               5 ((1, 2, 3))
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
             126 LOAD_CONST              15 (None)
             128 RETURN_VALUE
'''

snapshots['test_function_call (1, 3, 7)'] = '''
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

snapshots['test_function_call_with_args (1, 3, 7)'] = '''
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
              58 LOAD_CONST               9 (1)
+             60 BUILD_LIST               2
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST              10 (131)
+             70 LOAD_CONST               9 (1)
+             72 LOAD_CONST              11 (6)
+             74 LOAD_CONST               4 (0)
+             76 LOAD_CONST               5 (False)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 LOAD_GLOBAL              2 (reversed)
+             84 ROT_TWO
+             86 CALL_FUNCTION            1
+             88 UNPACK_SEQUENCE          2
              90 CALL_FUNCTION            1
+             92 BUILD_LIST               1
+             94 DUP_TOP
+             96 LOAD_GLOBAL              0 (py_instrument_receiver)
+             98 ROT_TWO
+            100 LOAD_CONST              10 (131)
+            102 LOAD_CONST               9 (1)
+            104 LOAD_CONST              11 (6)
+            106 LOAD_CONST               4 (0)
+            108 LOAD_CONST               8 (True)
+            110 CALL_FUNCTION            6
+            112 POP_TOP
+            114 UNPACK_SEQUENCE          1
             116 POP_TOP
             118 LOAD_CONST              12 (None)
             120 RETURN_VALUE

Code Object: f
   3           0 LOAD_FAST                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (124)
+             12 LOAD_CONST               1 ('x')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               3 (1)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 RETURN_VALUE
'''

snapshots['test_inner_function (1, 3, 7)'] = '''
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

snapshots['test_inner_function_nonlocal_ref (1, 3, 7)'] = '''
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
   7          32 LOAD_NAME                1 (f)
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
              58 LOAD_CONST               9 (1)
+             60 BUILD_LIST               2
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST              10 (131)
+             70 LOAD_CONST               9 (1)
+             72 LOAD_CONST              11 (6)
+             74 LOAD_CONST               4 (0)
+             76 LOAD_CONST               5 (False)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 LOAD_GLOBAL              2 (reversed)
+             84 ROT_TWO
+             86 CALL_FUNCTION            1
+             88 UNPACK_SEQUENCE          2
              90 CALL_FUNCTION            1
+             92 BUILD_LIST               1
+             94 DUP_TOP
+             96 LOAD_GLOBAL              0 (py_instrument_receiver)
+             98 ROT_TWO
+            100 LOAD_CONST              10 (131)
+            102 LOAD_CONST               9 (1)
+            104 LOAD_CONST              11 (6)
+            106 LOAD_CONST               4 (0)
+            108 LOAD_CONST               8 (True)
+            110 CALL_FUNCTION            6
+            112 POP_TOP
+            114 UNPACK_SEQUENCE          1
             116 POP_TOP
             118 LOAD_CONST              12 (None)
             120 RETURN_VALUE

Code Object: f
   3           0 LOAD_CLOSURE             0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (135)
+             12 LOAD_CONST               1 ('cell')
+             14 LOAD_CONST               2 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               3 (0)
+             20 LOAD_CONST               4 (1)
+             22 LOAD_CONST               5 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 BUILD_TUPLE              1
~             32 LOAD_CONST               6 (<code object g at SOME ADDRESS, file "<string>", line 3>)
              34 LOAD_CONST               7 ('f.<locals>.g')
              36 MAKE_FUNCTION            8
+             38 BUILD_LIST               1
+             40 DUP_TOP
+             42 LOAD_GLOBAL              0 (py_instrument_receiver)
+             44 ROT_TWO
+             46 LOAD_CONST               8 (125)
+             48 LOAD_CONST               9 ('g')
+             50 LOAD_CONST              10 (5)
+             52 LOAD_CONST               4 (1)
+             54 LOAD_CONST              11 (False)
+             56 CALL_FUNCTION            6
+             58 POP_TOP
+             60 UNPACK_SEQUENCE          1
              62 STORE_FAST               1 (g)
   6          64 LOAD_FAST                1 (g)
+             66 BUILD_LIST               1
+             68 DUP_TOP
+             70 LOAD_GLOBAL              0 (py_instrument_receiver)
+             72 ROT_TWO
+             74 LOAD_CONST              12 (124)
+             76 LOAD_CONST               9 ('g')
+             78 LOAD_CONST              13 (6)
+             80 LOAD_CONST               4 (1)
+             82 LOAD_CONST               5 (True)
+             84 CALL_FUNCTION            6
+             86 POP_TOP
+             88 UNPACK_SEQUENCE          1
+             90 BUILD_LIST               1
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST              14 (131)
+            100 LOAD_CONST               3 (0)
+            102 LOAD_CONST              15 (7)
+            104 LOAD_CONST               4 (1)
+            106 LOAD_CONST              11 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
             114 CALL_FUNCTION            0
+            116 BUILD_LIST               1
+            118 DUP_TOP
+            120 LOAD_GLOBAL              0 (py_instrument_receiver)
+            122 ROT_TWO
+            124 LOAD_CONST              14 (131)
+            126 LOAD_CONST               3 (0)
+            128 LOAD_CONST              15 (7)
+            130 LOAD_CONST               4 (1)
+            132 LOAD_CONST               5 (True)
+            134 CALL_FUNCTION            6
+            136 POP_TOP
+            138 UNPACK_SEQUENCE          1
             140 POP_TOP
             142 LOAD_CONST              16 (None)
             144 RETURN_VALUE

Code Object: g
   5           0 LOAD_DEREF               0 (i)
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

snapshots['test_load_name (2, 3, 7)'] = [
    {
        'arg': 'list',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 0,
        'stack': [
            GenericRepr("<class 'list'>")
        ]
    }
]

snapshots['test_store_name (2, 3, 7)'] = [
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 26,
        'stack': [
            1
        ]
    }
]

snapshots['test_load_attr (2, 3, 7)'] = [
    {
        'arg': 'range',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 0,
        'stack': [
            GenericRepr("<class 'range'>")
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 60,
        'stack': [
            GenericRepr("<class 'range'>"),
            0,
            5
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 60,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 110,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 112,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'start',
        'code': '<module>',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'orig_op': 162,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'start',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'orig_op': 162,
        'stack': [
            0
        ]
    }
]

snapshots['test_store_attr (2, 3, 7)'] = [
    {
        'arg': 'type',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 0,
        'stack': [
            GenericRepr("<class 'type'>")
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 62,
        'stack': [
            GenericRepr("<class 'type'>"),
            '',
            (
            ),
            {
            }
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 62,
        'stack': [
            GenericRepr("<class ''>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 112,
        'stack': [
            GenericRepr("<class ''>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 112,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 162,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 166,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 'a',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_ATTR',
        'orig_op': 222,
        'stack': [
            1,
            GenericRepr('< object at 0x100000000>')
        ]
    }
]

snapshots['test_store_then_load (2, 3, 7)'] = [
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 26,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 28,
        'stack': [
            1
        ]
    }
]

snapshots['test_list_load (2, 3, 7)'] = [
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 32,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 34,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 92,
        'stack': [
            [
                1,
                2,
                3
            ],
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 92,
        'stack': [
            2
        ]
    }
]

snapshots['test_list_store (2, 3, 7)'] = [
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 32,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 36,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 94,
        'stack': [
            2,
            [
                1,
                2,
                3
            ],
            1
        ]
    }
]

snapshots['test_for_loop (2, 3, 7)'] = [
    {
        'arg': {
            'label': 126
        },
        'code': '<module>',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 22,
        'stack': [
        ]
    },
    {
        'arrive_at': 50
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 76,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 50
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 76,
        'stack': [
            2
        ]
    },
    {
        'arrive_at': 50
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 76,
        'stack': [
            3
        ]
    },
    {
        'arrive_at': 50
    },
    {
        'arrive_at': 102
    },
    {
        'arrive_at': 126
    }
]

snapshots['test_function_call (2, 3, 7)'] = [
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            None
        ]
    }
]

snapshots['test_function_call_with_args (2, 3, 7)'] = [
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            GenericRepr('<function f at 0x100000000>'),
            1
        ]
    },
    {
        'arg': 'x',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            1
        ]
    }
]

snapshots['test_inner_function (2, 3, 7)'] = [
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 30,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 32,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            None
        ]
    }
]

snapshots['test_inner_function_nonlocal_ref (2, 3, 7)'] = [
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            GenericRepr('<function f at 0x100000000>')
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            GenericRepr('<function f at 0x100000000>'),
            1
        ]
    },
    {
        'arg': {
            'cell': 'i'
        },
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 0,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 62,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 64,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 114,
        'stack': [
            GenericRepr('<function f.<locals>.g at 0x100000000>')
        ]
    },
    {
        'arg': {
            'free': 'i'
        },
        'code': 'g',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 114,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            None
        ]
    }
]
