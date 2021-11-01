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
+             10 LOAD_CONST               1 (101)
+             12 LOAD_CONST               2 ('list')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               3 (0)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 POP_TOP
+             28 LOAD_GLOBAL              1 (py_instrument_receiver)
+             30 BUILD_LIST               0
+             32 LOAD_CONST               5 (1)
+             34 LOAD_CONST               0 (None)
+             36 LOAD_CONST               5 (1)
+             38 LOAD_CONST               3 (0)
+             40 LOAD_CONST               4 (True)
+             42 CALL_FUNCTION            6
+             44 POP_TOP
              46 LOAD_CONST               0 (None)
+             48 BUILD_LIST               1
+             50 DUP_TOP
+             52 LOAD_GLOBAL              1 (py_instrument_receiver)
+             54 ROT_TWO
+             56 LOAD_CONST               6 (100)
+             58 LOAD_CONST               0 (None)
+             60 LOAD_CONST               7 (2)
+             62 LOAD_CONST               3 (0)
+             64 LOAD_CONST               4 (True)
+             66 CALL_FUNCTION            6
+             68 POP_TOP
+             70 UNPACK_SEQUENCE          1
              72 RETURN_VALUE
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
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 26,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 46,
        'stack': [
            None
        ]
    }
]

snapshots['test_store_name (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               4 (90)
+             36 LOAD_CONST               5 ('x')
+             38 LOAD_CONST               0 (1)
+             40 LOAD_CONST               2 (0)
+             42 LOAD_CONST               6 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_NAME               1 (x)
              52 LOAD_CONST               7 (None)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               7 (None)
+             66 LOAD_CONST               8 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 RETURN_VALUE
'''

snapshots['test_store_name (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            None
        ]
    }
]

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
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              1 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               4 (100)
+             38 LOAD_CONST               2 (0)
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               6 (5)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               4 (100)
+             64 LOAD_CONST               6 (5)
+             66 LOAD_CONST               7 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               3
+             80 DUP_TOP
+             82 LOAD_GLOBAL              1 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               8 (131)
+             88 LOAD_CONST               7 (2)
+             90 LOAD_CONST               9 (3)
+             92 LOAD_CONST               2 (0)
+             94 LOAD_CONST              10 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 LOAD_GLOBAL              2 (reversed)
+            102 ROT_TWO
+            104 CALL_FUNCTION            1
+            106 UNPACK_SEQUENCE          3
             108 CALL_FUNCTION            2
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST               8 (131)
+            120 LOAD_CONST               7 (2)
+            122 LOAD_CONST               9 (3)
+            124 LOAD_CONST               2 (0)
+            126 LOAD_CONST               3 (True)
+            128 CALL_FUNCTION            6
+            130 POP_TOP
+            132 UNPACK_SEQUENCE          1
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              1 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST              11 (90)
+            144 LOAD_CONST              12 ('x')
+            146 LOAD_CONST              13 (4)
+            148 LOAD_CONST               2 (0)
+            150 LOAD_CONST              10 (False)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
+            156 UNPACK_SEQUENCE          1
             158 STORE_NAME               3 (x)
   3         160 LOAD_NAME                3 (x)
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              1 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST               0 (101)
+            172 LOAD_CONST              12 ('x')
+            174 LOAD_CONST               6 (5)
+            176 LOAD_CONST               2 (0)
+            178 LOAD_CONST               3 (True)
+            180 CALL_FUNCTION            6
+            182 POP_TOP
+            184 UNPACK_SEQUENCE          1
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              1 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              14 (106)
+            196 LOAD_CONST              15 ('start')
+            198 LOAD_CONST              16 (6)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST              10 (False)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
             210 LOAD_ATTR                4 (start)
+            212 BUILD_LIST               1
+            214 DUP_TOP
+            216 LOAD_GLOBAL              1 (py_instrument_receiver)
+            218 ROT_TWO
+            220 LOAD_CONST              14 (106)
+            222 LOAD_CONST              15 ('start')
+            224 LOAD_CONST              16 (6)
+            226 LOAD_CONST               2 (0)
+            228 LOAD_CONST               3 (True)
+            230 CALL_FUNCTION            6
+            232 POP_TOP
+            234 UNPACK_SEQUENCE          1
             236 POP_TOP
+            238 LOAD_GLOBAL              1 (py_instrument_receiver)
+            240 BUILD_LIST               0
+            242 LOAD_CONST               5 (1)
+            244 LOAD_CONST              17 (None)
+            246 LOAD_CONST              18 (7)
+            248 LOAD_CONST               2 (0)
+            250 LOAD_CONST               3 (True)
+            252 CALL_FUNCTION            6
+            254 POP_TOP
             256 LOAD_CONST              17 (None)
+            258 BUILD_LIST               1
+            260 DUP_TOP
+            262 LOAD_GLOBAL              1 (py_instrument_receiver)
+            264 ROT_TWO
+            266 LOAD_CONST               4 (100)
+            268 LOAD_CONST              17 (None)
+            270 LOAD_CONST              19 (8)
+            272 LOAD_CONST               2 (0)
+            274 LOAD_CONST               3 (True)
+            276 CALL_FUNCTION            6
+            278 POP_TOP
+            280 UNPACK_SEQUENCE          1
             282 RETURN_VALUE
'''

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
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': 5,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            5
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 108,
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
        'orig_op': 108,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 158,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 160,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'start',
        'code': '<module>',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'orig_op': 210,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 'start',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'orig_op': 210,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 236,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 256,
        'stack': [
            None
        ]
    }
]

snapshots['test_store_attr (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (type)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (101)
+             12 LOAD_CONST               2 ('type')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               3 (0)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               0 ('')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              1 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               5 (100)
+             38 LOAD_CONST               0 ('')
+             40 LOAD_CONST               6 (1)
+             42 LOAD_CONST               3 (0)
+             44 LOAD_CONST               4 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               7 (())
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               5 (100)
+             64 LOAD_CONST               7 (())
+             66 LOAD_CONST               8 (2)
+             68 LOAD_CONST               3 (0)
+             70 LOAD_CONST               4 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 BUILD_MAP                0
+             80 BUILD_LIST               4
+             82 DUP_TOP
+             84 LOAD_GLOBAL              1 (py_instrument_receiver)
+             86 ROT_TWO
+             88 LOAD_CONST               9 (131)
+             90 LOAD_CONST              10 (3)
+             92 LOAD_CONST              11 (4)
+             94 LOAD_CONST               3 (0)
+             96 LOAD_CONST              12 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 LOAD_GLOBAL              2 (reversed)
+            104 ROT_TWO
+            106 CALL_FUNCTION            1
+            108 UNPACK_SEQUENCE          4
             110 CALL_FUNCTION            3
+            112 BUILD_LIST               1
+            114 DUP_TOP
+            116 LOAD_GLOBAL              1 (py_instrument_receiver)
+            118 ROT_TWO
+            120 LOAD_CONST               9 (131)
+            122 LOAD_CONST              10 (3)
+            124 LOAD_CONST              11 (4)
+            126 LOAD_CONST               3 (0)
+            128 LOAD_CONST               4 (True)
+            130 CALL_FUNCTION            6
+            132 POP_TOP
+            134 UNPACK_SEQUENCE          1
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              1 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST               9 (131)
+            146 LOAD_CONST               3 (0)
+            148 LOAD_CONST              13 (5)
+            150 LOAD_CONST               3 (0)
+            152 LOAD_CONST              12 (False)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
             160 CALL_FUNCTION            0
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              1 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST               9 (131)
+            172 LOAD_CONST               3 (0)
+            174 LOAD_CONST              13 (5)
+            176 LOAD_CONST               3 (0)
+            178 LOAD_CONST               4 (True)
+            180 CALL_FUNCTION            6
+            182 POP_TOP
+            184 UNPACK_SEQUENCE          1
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              1 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              14 (90)
+            196 LOAD_CONST              15 ('x')
+            198 LOAD_CONST              16 (6)
+            200 LOAD_CONST               3 (0)
+            202 LOAD_CONST              12 (False)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
             210 STORE_NAME               3 (x)
   3         212 LOAD_CONST               6 (1)
+            214 BUILD_LIST               1
+            216 DUP_TOP
+            218 LOAD_GLOBAL              1 (py_instrument_receiver)
+            220 ROT_TWO
+            222 LOAD_CONST               5 (100)
+            224 LOAD_CONST               6 (1)
+            226 LOAD_CONST              17 (7)
+            228 LOAD_CONST               3 (0)
+            230 LOAD_CONST               4 (True)
+            232 CALL_FUNCTION            6
+            234 POP_TOP
+            236 UNPACK_SEQUENCE          1
             238 LOAD_NAME                3 (x)
+            240 BUILD_LIST               1
+            242 DUP_TOP
+            244 LOAD_GLOBAL              1 (py_instrument_receiver)
+            246 ROT_TWO
+            248 LOAD_CONST               1 (101)
+            250 LOAD_CONST              15 ('x')
+            252 LOAD_CONST              18 (8)
+            254 LOAD_CONST               3 (0)
+            256 LOAD_CONST               4 (True)
+            258 CALL_FUNCTION            6
+            260 POP_TOP
+            262 UNPACK_SEQUENCE          1
+            264 BUILD_LIST               2
+            266 DUP_TOP
+            268 LOAD_GLOBAL              1 (py_instrument_receiver)
+            270 ROT_TWO
+            272 LOAD_CONST              19 (95)
+            274 LOAD_CONST              20 ('a')
+            276 LOAD_CONST              21 (9)
+            278 LOAD_CONST               3 (0)
+            280 LOAD_CONST              12 (False)
+            282 CALL_FUNCTION            6
+            284 POP_TOP
+            286 LOAD_GLOBAL              2 (reversed)
+            288 ROT_TWO
+            290 CALL_FUNCTION            1
+            292 UNPACK_SEQUENCE          2
             294 STORE_ATTR               4 (a)
             296 LOAD_CONST              22 (None)
+            298 BUILD_LIST               1
+            300 DUP_TOP
+            302 LOAD_GLOBAL              1 (py_instrument_receiver)
+            304 ROT_TWO
+            306 LOAD_CONST               5 (100)
+            308 LOAD_CONST              22 (None)
+            310 LOAD_CONST              23 (10)
+            312 LOAD_CONST               3 (0)
+            314 LOAD_CONST               4 (True)
+            316 CALL_FUNCTION            6
+            318 POP_TOP
+            320 UNPACK_SEQUENCE          1
             322 RETURN_VALUE
'''

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
        'arg': '',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            ''
        ]
    },
    {
        'arg': (
        ),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            (
            )
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 110,
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
        'orig_op': 110,
        'stack': [
            GenericRepr("<class ''>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 160,
        'stack': [
            GenericRepr("<class ''>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 160,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 210,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 212,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 238,
        'stack': [
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': 'a',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_ATTR',
        'orig_op': 294,
        'stack': [
            1,
            GenericRepr('< object at 0x100000000>')
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 296,
        'stack': [
            None
        ]
    }
]

snapshots['test_store_then_load (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               4 (90)
+             36 LOAD_CONST               5 ('x')
+             38 LOAD_CONST               0 (1)
+             40 LOAD_CONST               2 (0)
+             42 LOAD_CONST               6 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_NAME               1 (x)
   3          52 LOAD_NAME                1 (x)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               7 (101)
+             64 LOAD_CONST               5 ('x')
+             66 LOAD_CONST               8 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 POP_TOP
+             80 LOAD_GLOBAL              0 (py_instrument_receiver)
+             82 BUILD_LIST               0
+             84 LOAD_CONST               0 (1)
+             86 LOAD_CONST               9 (None)
+             88 LOAD_CONST              10 (3)
+             90 LOAD_CONST               2 (0)
+             92 LOAD_CONST               3 (True)
+             94 CALL_FUNCTION            6
+             96 POP_TOP
              98 LOAD_CONST               9 (None)
+            100 BUILD_LIST               1
+            102 DUP_TOP
+            104 LOAD_GLOBAL              0 (py_instrument_receiver)
+            106 ROT_TWO
+            108 LOAD_CONST               1 (100)
+            110 LOAD_CONST               9 (None)
+            112 LOAD_CONST              11 (4)
+            114 LOAD_CONST               2 (0)
+            116 LOAD_CONST               3 (True)
+            118 CALL_FUNCTION            6
+            120 POP_TOP
+            122 UNPACK_SEQUENCE          1
             124 RETURN_VALUE
'''

snapshots['test_store_then_load (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 52,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 78,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 98,
        'stack': [
            None
        ]
    }
]

snapshots['test_list_load (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 (2)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 (2)
+             40 LOAD_CONST               0 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               5 (3)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               5 (3)
+             66 LOAD_CONST               4 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 BUILD_LIST               3
+             80 BUILD_LIST               1
+             82 DUP_TOP
+             84 LOAD_GLOBAL              0 (py_instrument_receiver)
+             86 ROT_TWO
+             88 LOAD_CONST               6 (90)
+             90 LOAD_CONST               7 ('arr')
+             92 LOAD_CONST               8 (4)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               9 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 UNPACK_SEQUENCE          1
             104 STORE_NAME               1 (arr)
   3         106 LOAD_NAME                1 (arr)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST              10 (101)
+            118 LOAD_CONST               7 ('arr')
+            120 LOAD_CONST              11 (5)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               3 (True)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 LOAD_CONST               0 (1)
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              0 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST               1 (100)
+            144 LOAD_CONST               0 (1)
+            146 LOAD_CONST              12 (6)
+            148 LOAD_CONST               2 (0)
+            150 LOAD_CONST               3 (True)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
+            156 UNPACK_SEQUENCE          1
+            158 BUILD_LIST               2
+            160 DUP_TOP
+            162 LOAD_GLOBAL              0 (py_instrument_receiver)
+            164 ROT_TWO
+            166 LOAD_CONST              13 (25)
+            168 LOAD_CONST              14 (None)
+            170 LOAD_CONST              15 (7)
+            172 LOAD_CONST               2 (0)
+            174 LOAD_CONST               9 (False)
+            176 CALL_FUNCTION            6
+            178 POP_TOP
+            180 LOAD_GLOBAL              2 (reversed)
+            182 ROT_TWO
+            184 CALL_FUNCTION            1
+            186 UNPACK_SEQUENCE          2
             188 BINARY_SUBSCR
+            190 BUILD_LIST               1
+            192 DUP_TOP
+            194 LOAD_GLOBAL              0 (py_instrument_receiver)
+            196 ROT_TWO
+            198 LOAD_CONST              13 (25)
+            200 LOAD_CONST              14 (None)
+            202 LOAD_CONST              15 (7)
+            204 LOAD_CONST               2 (0)
+            206 LOAD_CONST               3 (True)
+            208 CALL_FUNCTION            6
+            210 POP_TOP
+            212 UNPACK_SEQUENCE          1
             214 POP_TOP
+            216 LOAD_GLOBAL              0 (py_instrument_receiver)
+            218 BUILD_LIST               0
+            220 LOAD_CONST               0 (1)
+            222 LOAD_CONST              14 (None)
+            224 LOAD_CONST              16 (8)
+            226 LOAD_CONST               2 (0)
+            228 LOAD_CONST               3 (True)
+            230 CALL_FUNCTION            6
+            232 POP_TOP
             234 LOAD_CONST              14 (None)
+            236 BUILD_LIST               1
+            238 DUP_TOP
+            240 LOAD_GLOBAL              0 (py_instrument_receiver)
+            242 ROT_TWO
+            244 LOAD_CONST               1 (100)
+            246 LOAD_CONST              14 (None)
+            248 LOAD_CONST              17 (9)
+            250 LOAD_CONST               2 (0)
+            252 LOAD_CONST               3 (True)
+            254 CALL_FUNCTION            6
+            256 POP_TOP
+            258 UNPACK_SEQUENCE          1
             260 RETURN_VALUE
'''

snapshots['test_list_load (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            3
        ]
    },
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 104,
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
        'orig_op': 106,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 132,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 188,
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
        'orig_op': 188,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 214,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 234,
        'stack': [
            None
        ]
    }
]

snapshots['test_list_store (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 (2)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 (2)
+             40 LOAD_CONST               0 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               5 (3)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               5 (3)
+             66 LOAD_CONST               4 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 BUILD_LIST               3
+             80 BUILD_LIST               1
+             82 DUP_TOP
+             84 LOAD_GLOBAL              0 (py_instrument_receiver)
+             86 ROT_TWO
+             88 LOAD_CONST               6 (90)
+             90 LOAD_CONST               7 ('arr')
+             92 LOAD_CONST               8 (4)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               9 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 UNPACK_SEQUENCE          1
             104 STORE_NAME               1 (arr)
   3         106 LOAD_CONST               4 (2)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               1 (100)
+            118 LOAD_CONST               4 (2)
+            120 LOAD_CONST              10 (5)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               3 (True)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 LOAD_NAME                1 (arr)
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              0 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST              11 (101)
+            144 LOAD_CONST               7 ('arr')
+            146 LOAD_CONST              12 (6)
+            148 LOAD_CONST               2 (0)
+            150 LOAD_CONST               3 (True)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
+            156 UNPACK_SEQUENCE          1
             158 LOAD_CONST               0 (1)
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST               1 (100)
+            170 LOAD_CONST               0 (1)
+            172 LOAD_CONST              13 (7)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               3 (True)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
+            184 BUILD_LIST               3
+            186 DUP_TOP
+            188 LOAD_GLOBAL              0 (py_instrument_receiver)
+            190 ROT_TWO
+            192 LOAD_CONST              14 (60)
+            194 LOAD_CONST              15 (None)
+            196 LOAD_CONST              16 (8)
+            198 LOAD_CONST               2 (0)
+            200 LOAD_CONST               9 (False)
+            202 CALL_FUNCTION            6
+            204 POP_TOP
+            206 LOAD_GLOBAL              2 (reversed)
+            208 ROT_TWO
+            210 CALL_FUNCTION            1
+            212 UNPACK_SEQUENCE          3
             214 STORE_SUBSCR
             216 LOAD_CONST              15 (None)
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST               1 (100)
+            228 LOAD_CONST              15 (None)
+            230 LOAD_CONST              17 (9)
+            232 LOAD_CONST               2 (0)
+            234 LOAD_CONST               3 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
             242 RETURN_VALUE
'''

snapshots['test_list_store (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            3
        ]
    },
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 104,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 106,
        'stack': [
            2
        ]
    },
    {
        'arg': 'arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 132,
        'stack': [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 158,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 214,
        'stack': [
            2,
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
        'opcode': 'LOAD_CONST',
        'orig_op': 216,
        'stack': [
            None
        ]
    }
]

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
              22 SETUP_LOOP             104 (to 128)
              24 LOAD_CONST               5 ((1, 2, 3))
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (100)
+             36 LOAD_CONST               5 ((1, 2, 3))
+             38 LOAD_CONST               7 (1)
+             40 LOAD_CONST               3 (0)
+             42 LOAD_CONST               8 (True)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 GET_ITER
+        >>   52 LOAD_GLOBAL              0 (py_instrument_receiver)
+             54 BUILD_LIST               0
+             56 LOAD_CONST               9 ('JUMP_TARGET')
+             58 LOAD_CONST               1 ('label')
+             60 LOAD_CONST              10 (4)
+             62 BUILD_MAP                1
+             64 LOAD_CONST              11 (3)
+             66 LOAD_CONST               3 (0)
+             68 LOAD_CONST               4 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
              74 FOR_ITER                28 (to 104)
+             76 BUILD_LIST               1
+             78 DUP_TOP
+             80 LOAD_GLOBAL              0 (py_instrument_receiver)
+             82 ROT_TWO
+             84 LOAD_CONST              12 (90)
+             86 LOAD_CONST              13 ('i')
+             88 LOAD_CONST              14 (5)
+             90 LOAD_CONST               3 (0)
+             92 LOAD_CONST               4 (False)
+             94 CALL_FUNCTION            6
+             96 POP_TOP
+             98 UNPACK_SEQUENCE          1
             100 STORE_NAME               1 (i)
   3         102 JUMP_ABSOLUTE           52
+        >>  104 LOAD_GLOBAL              0 (py_instrument_receiver)
+            106 BUILD_LIST               0
+            108 LOAD_CONST               9 ('JUMP_TARGET')
+            110 LOAD_CONST               1 ('label')
+            112 LOAD_CONST              15 (8)
+            114 BUILD_MAP                1
+            116 LOAD_CONST              16 (7)
+            118 LOAD_CONST               3 (0)
+            120 LOAD_CONST               4 (False)
+            122 CALL_FUNCTION            6
+            124 POP_TOP
             126 POP_BLOCK
+        >>  128 LOAD_GLOBAL              0 (py_instrument_receiver)
+            130 BUILD_LIST               0
+            132 LOAD_CONST               9 ('JUMP_TARGET')
+            134 LOAD_CONST               1 ('label')
+            136 LOAD_CONST               2 (10)
+            138 BUILD_MAP                1
+            140 LOAD_CONST              17 (9)
+            142 LOAD_CONST               3 (0)
+            144 LOAD_CONST               4 (False)
+            146 CALL_FUNCTION            6
+            148 POP_TOP
             150 LOAD_CONST              18 (None)
+            152 BUILD_LIST               1
+            154 DUP_TOP
+            156 LOAD_GLOBAL              0 (py_instrument_receiver)
+            158 ROT_TWO
+            160 LOAD_CONST               6 (100)
+            162 LOAD_CONST              18 (None)
+            164 LOAD_CONST               2 (10)
+            166 LOAD_CONST               3 (0)
+            168 LOAD_CONST               8 (True)
+            170 CALL_FUNCTION            6
+            172 POP_TOP
+            174 UNPACK_SEQUENCE          1
             176 RETURN_VALUE
'''

snapshots['test_for_loop (2, 3, 7)'] = [
    {
        'arg': {
            'label': 150
        },
        'code': '<module>',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 22,
        'stack': [
        ]
    },
    {
        'arg': (
            1,
            2,
            3
        ),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 24,
        'stack': [
            (
                1,
                2,
                3
            )
        ]
    },
    {
        'arrive_at': 74
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 100,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 74
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 100,
        'stack': [
            2
        ]
    },
    {
        'arrive_at': 74
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 100,
        'stack': [
            3
        ]
    },
    {
        'arrive_at': 74
    },
    {
        'arrive_at': 126
    },
    {
        'arrive_at': 150
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 150,
        'stack': [
            None
        ]
    }
]

snapshots['test_function_call (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 MAKE_FUNCTION            0
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               6 (90)
+             64 LOAD_CONST               4 ('f')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (f)
   4          80 LOAD_NAME                1 (f)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('f')
+             94 LOAD_CONST              10 (4)
+             96 LOAD_CONST               2 (0)
+             98 LOAD_CONST               3 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST              11 (131)
+            116 LOAD_CONST               2 (0)
+            118 LOAD_CONST              12 (5)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               8 (False)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
             130 CALL_FUNCTION            0
+            132 BUILD_LIST               1
+            134 DUP_TOP
+            136 LOAD_GLOBAL              0 (py_instrument_receiver)
+            138 ROT_TWO
+            140 LOAD_CONST              11 (131)
+            142 LOAD_CONST               2 (0)
+            144 LOAD_CONST              12 (5)
+            146 LOAD_CONST               2 (0)
+            148 LOAD_CONST               3 (True)
+            150 CALL_FUNCTION            6
+            152 POP_TOP
+            154 UNPACK_SEQUENCE          1
             156 POP_TOP
+            158 LOAD_GLOBAL              0 (py_instrument_receiver)
+            160 BUILD_LIST               0
+            162 LOAD_CONST               5 (1)
+            164 LOAD_CONST              13 (None)
+            166 LOAD_CONST              14 (6)
+            168 LOAD_CONST               2 (0)
+            170 LOAD_CONST               3 (True)
+            172 CALL_FUNCTION            6
+            174 POP_TOP
             176 LOAD_CONST              13 (None)
+            178 BUILD_LIST               1
+            180 DUP_TOP
+            182 LOAD_GLOBAL              0 (py_instrument_receiver)
+            184 ROT_TWO
+            186 LOAD_CONST               1 (100)
+            188 LOAD_CONST              13 (None)
+            190 LOAD_CONST              15 (7)
+            192 LOAD_CONST               2 (0)
+            194 LOAD_CONST               3 (True)
+            196 CALL_FUNCTION            6
+            198 POP_TOP
+            200 UNPACK_SEQUENCE          1
             202 RETURN_VALUE

Code Object: f
   3           0 LOAD_CONST               0 (None)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (None)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               3 (1)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 RETURN_VALUE
'''

snapshots['test_function_call (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 156,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 176,
        'stack': [
            None
        ]
    }
]

snapshots['test_function_call_with_args (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 MAKE_FUNCTION            0
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               6 (90)
+             64 LOAD_CONST               4 ('f')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (f)
   4          80 LOAD_NAME                1 (f)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('f')
+             94 LOAD_CONST              10 (4)
+             96 LOAD_CONST               2 (0)
+             98 LOAD_CONST               3 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 LOAD_CONST               5 (1)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               1 (100)
+            118 LOAD_CONST               5 (1)
+            120 LOAD_CONST              11 (5)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               3 (True)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
+            132 BUILD_LIST               2
+            134 DUP_TOP
+            136 LOAD_GLOBAL              0 (py_instrument_receiver)
+            138 ROT_TWO
+            140 LOAD_CONST              12 (131)
+            142 LOAD_CONST               5 (1)
+            144 LOAD_CONST              13 (6)
+            146 LOAD_CONST               2 (0)
+            148 LOAD_CONST               8 (False)
+            150 CALL_FUNCTION            6
+            152 POP_TOP
+            154 LOAD_GLOBAL              2 (reversed)
+            156 ROT_TWO
+            158 CALL_FUNCTION            1
+            160 UNPACK_SEQUENCE          2
             162 CALL_FUNCTION            1
+            164 BUILD_LIST               1
+            166 DUP_TOP
+            168 LOAD_GLOBAL              0 (py_instrument_receiver)
+            170 ROT_TWO
+            172 LOAD_CONST              12 (131)
+            174 LOAD_CONST               5 (1)
+            176 LOAD_CONST              13 (6)
+            178 LOAD_CONST               2 (0)
+            180 LOAD_CONST               3 (True)
+            182 CALL_FUNCTION            6
+            184 POP_TOP
+            186 UNPACK_SEQUENCE          1
             188 POP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 BUILD_LIST               0
+            194 LOAD_CONST               5 (1)
+            196 LOAD_CONST              14 (None)
+            198 LOAD_CONST              15 (7)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
             208 LOAD_CONST              14 (None)
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               1 (100)
+            220 LOAD_CONST              14 (None)
+            222 LOAD_CONST              16 (8)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               3 (True)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 RETURN_VALUE

Code Object: f
   3           0 LOAD_FAST                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (124)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 RETURN_VALUE
'''

snapshots['test_function_call_with_args (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 106,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            '<function f at SOME ADDRESS>',
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
        'orig_op': 162,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 188,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 208,
        'stack': [
            None
        ]
    }
]

snapshots['test_inner_function (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 MAKE_FUNCTION            0
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               6 (90)
+             64 LOAD_CONST               4 ('f')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (f)
   6          80 LOAD_NAME                1 (f)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('f')
+             94 LOAD_CONST              10 (4)
+             96 LOAD_CONST               2 (0)
+             98 LOAD_CONST               3 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST              11 (131)
+            116 LOAD_CONST               2 (0)
+            118 LOAD_CONST              12 (5)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               8 (False)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
             130 CALL_FUNCTION            0
+            132 BUILD_LIST               1
+            134 DUP_TOP
+            136 LOAD_GLOBAL              0 (py_instrument_receiver)
+            138 ROT_TWO
+            140 LOAD_CONST              11 (131)
+            142 LOAD_CONST               2 (0)
+            144 LOAD_CONST              12 (5)
+            146 LOAD_CONST               2 (0)
+            148 LOAD_CONST               3 (True)
+            150 CALL_FUNCTION            6
+            152 POP_TOP
+            154 UNPACK_SEQUENCE          1
             156 POP_TOP
+            158 LOAD_GLOBAL              0 (py_instrument_receiver)
+            160 BUILD_LIST               0
+            162 LOAD_CONST               5 (1)
+            164 LOAD_CONST              13 (None)
+            166 LOAD_CONST              14 (6)
+            168 LOAD_CONST               2 (0)
+            170 LOAD_CONST               3 (True)
+            172 CALL_FUNCTION            6
+            174 POP_TOP
             176 LOAD_CONST              13 (None)
+            178 BUILD_LIST               1
+            180 DUP_TOP
+            182 LOAD_GLOBAL              0 (py_instrument_receiver)
+            184 ROT_TWO
+            186 LOAD_CONST               1 (100)
+            188 LOAD_CONST              13 (None)
+            190 LOAD_CONST              15 (7)
+            192 LOAD_CONST               2 (0)
+            194 LOAD_CONST               3 (True)
+            196 CALL_FUNCTION            6
+            198 POP_TOP
+            200 UNPACK_SEQUENCE          1
             202 RETURN_VALUE

Code Object: f
~  3           0 LOAD_CONST               1 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (100)
+             12 LOAD_CONST               1 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               6 ('f.<locals>.g')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               2 (100)
+             38 LOAD_CONST               6 ('f.<locals>.g')
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               4 (1)
+             44 LOAD_CONST               5 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 MAKE_FUNCTION            0
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               7 (125)
+             64 LOAD_CONST               8 ('g')
+             66 LOAD_CONST               9 (3)
+             68 LOAD_CONST               4 (1)
+             70 LOAD_CONST              10 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_FAST               0 (g)
   5          80 LOAD_FAST                0 (g)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST              11 (124)
+             92 LOAD_CONST               8 ('g')
+             94 LOAD_CONST              12 (4)
+             96 LOAD_CONST               4 (1)
+             98 LOAD_CONST               5 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST              13 (131)
+            116 LOAD_CONST               3 (0)
+            118 LOAD_CONST              14 (5)
+            120 LOAD_CONST               4 (1)
+            122 LOAD_CONST              10 (False)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
             130 CALL_FUNCTION            0
+            132 BUILD_LIST               1
+            134 DUP_TOP
+            136 LOAD_GLOBAL              0 (py_instrument_receiver)
+            138 ROT_TWO
+            140 LOAD_CONST              13 (131)
+            142 LOAD_CONST               3 (0)
+            144 LOAD_CONST              14 (5)
+            146 LOAD_CONST               4 (1)
+            148 LOAD_CONST               5 (True)
+            150 CALL_FUNCTION            6
+            152 POP_TOP
+            154 UNPACK_SEQUENCE          1
             156 POP_TOP
+            158 LOAD_GLOBAL              0 (py_instrument_receiver)
+            160 BUILD_LIST               0
+            162 LOAD_CONST               4 (1)
+            164 LOAD_CONST               0 (None)
+            166 LOAD_CONST              15 (6)
+            168 LOAD_CONST               4 (1)
+            170 LOAD_CONST               5 (True)
+            172 CALL_FUNCTION            6
+            174 POP_TOP
             176 LOAD_CONST               0 (None)
+            178 BUILD_LIST               1
+            180 DUP_TOP
+            182 LOAD_GLOBAL              0 (py_instrument_receiver)
+            184 ROT_TWO
+            186 LOAD_CONST               2 (100)
+            188 LOAD_CONST               0 (None)
+            190 LOAD_CONST              16 (7)
+            192 LOAD_CONST               4 (1)
+            194 LOAD_CONST               5 (True)
+            196 CALL_FUNCTION            6
+            198 POP_TOP
+            200 UNPACK_SEQUENCE          1
             202 RETURN_VALUE

Code Object: g
   4           0 LOAD_CONST               0 (None)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (None)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               3 (2)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 RETURN_VALUE
'''

snapshots['test_inner_function (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>')
        ]
    },
    {
        'arg': 'f.<locals>.g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f.<locals>.g'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 78,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 80,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': None,
        'code': 'g',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 156,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 176,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 156,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 176,
        'stack': [
            None
        ]
    }
]

snapshots['test_inner_function_nonlocal_ref (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 MAKE_FUNCTION            0
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               6 (90)
+             64 LOAD_CONST               4 ('f')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (f)
   7          80 LOAD_NAME                1 (f)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('f')
+             94 LOAD_CONST              10 (4)
+             96 LOAD_CONST               2 (0)
+             98 LOAD_CONST               3 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 LOAD_CONST               5 (1)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               1 (100)
+            118 LOAD_CONST               5 (1)
+            120 LOAD_CONST              11 (5)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               3 (True)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
+            132 BUILD_LIST               2
+            134 DUP_TOP
+            136 LOAD_GLOBAL              0 (py_instrument_receiver)
+            138 ROT_TWO
+            140 LOAD_CONST              12 (131)
+            142 LOAD_CONST               5 (1)
+            144 LOAD_CONST              13 (6)
+            146 LOAD_CONST               2 (0)
+            148 LOAD_CONST               8 (False)
+            150 CALL_FUNCTION            6
+            152 POP_TOP
+            154 LOAD_GLOBAL              2 (reversed)
+            156 ROT_TWO
+            158 CALL_FUNCTION            1
+            160 UNPACK_SEQUENCE          2
             162 CALL_FUNCTION            1
+            164 BUILD_LIST               1
+            166 DUP_TOP
+            168 LOAD_GLOBAL              0 (py_instrument_receiver)
+            170 ROT_TWO
+            172 LOAD_CONST              12 (131)
+            174 LOAD_CONST               5 (1)
+            176 LOAD_CONST              13 (6)
+            178 LOAD_CONST               2 (0)
+            180 LOAD_CONST               3 (True)
+            182 CALL_FUNCTION            6
+            184 POP_TOP
+            186 UNPACK_SEQUENCE          1
             188 POP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 BUILD_LIST               0
+            194 LOAD_CONST               5 (1)
+            196 LOAD_CONST              14 (None)
+            198 LOAD_CONST              15 (7)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
             208 LOAD_CONST              14 (None)
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               1 (100)
+            220 LOAD_CONST              14 (None)
+            222 LOAD_CONST              16 (8)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               3 (True)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 RETURN_VALUE

Code Object: f
   3           0 LOAD_CLOSURE             0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (135)
+             12 LOAD_CONST               2 ('cell')
+             14 LOAD_CONST               3 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               4 (0)
+             20 LOAD_CONST               5 (1)
+             22 LOAD_CONST               6 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 BUILD_TUPLE              1
~             32 LOAD_CONST               7 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               8 (100)
+             44 LOAD_CONST               7 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             46 LOAD_CONST               9 (2)
+             48 LOAD_CONST               5 (1)
+             50 LOAD_CONST               6 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
              58 LOAD_CONST              10 ('f.<locals>.g')
+             60 BUILD_LIST               1
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST               8 (100)
+             70 LOAD_CONST              10 ('f.<locals>.g')
+             72 LOAD_CONST              11 (3)
+             74 LOAD_CONST               5 (1)
+             76 LOAD_CONST               6 (True)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 UNPACK_SEQUENCE          1
              84 MAKE_FUNCTION            8
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              0 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST              12 (125)
+             96 LOAD_CONST              13 ('g')
+             98 LOAD_CONST              14 (5)
+            100 LOAD_CONST               5 (1)
+            102 LOAD_CONST              15 (False)
+            104 CALL_FUNCTION            6
+            106 POP_TOP
+            108 UNPACK_SEQUENCE          1
             110 STORE_FAST               1 (g)
   6         112 LOAD_FAST                1 (g)
+            114 BUILD_LIST               1
+            116 DUP_TOP
+            118 LOAD_GLOBAL              0 (py_instrument_receiver)
+            120 ROT_TWO
+            122 LOAD_CONST              16 (124)
+            124 LOAD_CONST              13 ('g')
+            126 LOAD_CONST              17 (6)
+            128 LOAD_CONST               5 (1)
+            130 LOAD_CONST               6 (True)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
+            138 BUILD_LIST               1
+            140 DUP_TOP
+            142 LOAD_GLOBAL              0 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST              18 (131)
+            148 LOAD_CONST               4 (0)
+            150 LOAD_CONST              19 (7)
+            152 LOAD_CONST               5 (1)
+            154 LOAD_CONST              15 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 UNPACK_SEQUENCE          1
             162 CALL_FUNCTION            0
+            164 BUILD_LIST               1
+            166 DUP_TOP
+            168 LOAD_GLOBAL              0 (py_instrument_receiver)
+            170 ROT_TWO
+            172 LOAD_CONST              18 (131)
+            174 LOAD_CONST               4 (0)
+            176 LOAD_CONST              19 (7)
+            178 LOAD_CONST               5 (1)
+            180 LOAD_CONST               6 (True)
+            182 CALL_FUNCTION            6
+            184 POP_TOP
+            186 UNPACK_SEQUENCE          1
             188 POP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 BUILD_LIST               0
+            194 LOAD_CONST               5 (1)
+            196 LOAD_CONST               0 (None)
+            198 LOAD_CONST              20 (8)
+            200 LOAD_CONST               5 (1)
+            202 LOAD_CONST               6 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
             208 LOAD_CONST               0 (None)
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               8 (100)
+            220 LOAD_CONST               0 (None)
+            222 LOAD_CONST              21 (9)
+            224 LOAD_CONST               5 (1)
+            226 LOAD_CONST               6 (True)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 RETURN_VALUE

Code Object: g
   5           0 LOAD_DEREF               0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (136)
+             12 LOAD_CONST               2 ('free')
+             14 LOAD_CONST               3 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               4 (0)
+             20 LOAD_CONST               5 (2)
+             22 LOAD_CONST               6 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 RETURN_VALUE
'''

snapshots['test_inner_function_nonlocal_ref (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 106,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            '<function f at SOME ADDRESS>',
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
        'arg': GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 32,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>')
        ]
    },
    {
        'arg': 'f.<locals>.g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 58,
        'stack': [
            'f.<locals>.g'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 110,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 112,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
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
        'orig_op': 162,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 188,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 208,
        'stack': [
            None
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 188,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 208,
        'stack': [
            None
        ]
    }
]
