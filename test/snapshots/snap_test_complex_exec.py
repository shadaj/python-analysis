# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_nested_iteration (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object myFunc at SOME ADDRESS, file "<string>", line 2>)
               2 LOAD_CONST               1 ('myFunc')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (90)
+             16 LOAD_CONST               1 ('myFunc')
+             18 LOAD_CONST               3 (3)
+             20 LOAD_CONST               4 (0)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_NAME               1 (myFunc)
  12          32 LOAD_NAME                1 (myFunc)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (101)
+             44 LOAD_CONST               1 ('myFunc')
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

Code Object: myFunc
   3           0 LOAD_CONST               1 (-1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (125)
+             12 LOAD_CONST               3 ('x')
+             14 LOAD_CONST               4 (1)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (False)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 STORE_FAST               0 (x)
   4          28 LOAD_GLOBAL              1 (list)
              30 LOAD_GLOBAL              2 (range)
              32 LOAD_CONST               6 (5)
+             34 BUILD_LIST               2
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               7 (131)
+             44 LOAD_CONST               4 (1)
+             46 LOAD_CONST               6 (5)
+             48 LOAD_CONST               4 (1)
+             50 LOAD_CONST               5 (False)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 LOAD_GLOBAL              3 (reversed)
+             58 ROT_TWO
+             60 CALL_FUNCTION            1
+             62 UNPACK_SEQUENCE          2
              64 CALL_FUNCTION            1
+             66 BUILD_LIST               1
+             68 DUP_TOP
+             70 LOAD_GLOBAL              0 (py_instrument_receiver)
+             72 ROT_TWO
+             74 LOAD_CONST               7 (131)
+             76 LOAD_CONST               4 (1)
+             78 LOAD_CONST               6 (5)
+             80 LOAD_CONST               4 (1)
+             82 LOAD_CONST               8 (True)
+             84 CALL_FUNCTION            6
+             86 POP_TOP
+             88 UNPACK_SEQUENCE          1
+             90 BUILD_LIST               2
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST               7 (131)
+            100 LOAD_CONST               4 (1)
+            102 LOAD_CONST               9 (6)
+            104 LOAD_CONST               4 (1)
+            106 LOAD_CONST               5 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 LOAD_GLOBAL              3 (reversed)
+            114 ROT_TWO
+            116 CALL_FUNCTION            1
+            118 UNPACK_SEQUENCE          2
             120 CALL_FUNCTION            1
+            122 BUILD_LIST               1
+            124 DUP_TOP
+            126 LOAD_GLOBAL              0 (py_instrument_receiver)
+            128 ROT_TWO
+            130 LOAD_CONST               7 (131)
+            132 LOAD_CONST               4 (1)
+            134 LOAD_CONST               9 (6)
+            136 LOAD_CONST               4 (1)
+            138 LOAD_CONST               8 (True)
+            140 CALL_FUNCTION            6
+            142 POP_TOP
+            144 UNPACK_SEQUENCE          1
+            146 BUILD_LIST               1
+            148 DUP_TOP
+            150 LOAD_GLOBAL              0 (py_instrument_receiver)
+            152 ROT_TWO
+            154 LOAD_CONST               2 (125)
+            156 LOAD_CONST              10 ('data')
+            158 LOAD_CONST              11 (7)
+            160 LOAD_CONST               4 (1)
+            162 LOAD_CONST               5 (False)
+            164 CALL_FUNCTION            6
+            166 POP_TOP
+            168 UNPACK_SEQUENCE          1
             170 STORE_FAST               1 (data)
+  5         172 LOAD_GLOBAL              0 (py_instrument_receiver)
+            174 BUILD_LIST               0
+            176 LOAD_CONST              12 (120)
+            178 LOAD_CONST              13 ('label')
+            180 LOAD_CONST              14 (43)
+            182 BUILD_MAP                1
+            184 LOAD_CONST              15 (8)
+            186 LOAD_CONST               4 (1)
+            188 LOAD_CONST               5 (False)
+            190 CALL_FUNCTION            6
+            192 POP_TOP
             194 EXTENDED_ARG             1
             196 SETUP_LOOP             432 (to 630)
+            198 LOAD_FAST                1 (data)
+            200 BUILD_LIST               1
+            202 DUP_TOP
+            204 LOAD_GLOBAL              0 (py_instrument_receiver)
+            206 ROT_TWO
+            208 LOAD_CONST              16 (124)
+            210 LOAD_CONST              10 ('data')
+            212 LOAD_CONST              17 (9)
+            214 LOAD_CONST               4 (1)
+            216 LOAD_CONST               8 (True)
+            218 CALL_FUNCTION            6
+            220 POP_TOP
             222 UNPACK_SEQUENCE          1
+            224 GET_ITER
+        >>  226 LOAD_GLOBAL              0 (py_instrument_receiver)
+            228 BUILD_LIST               0
+            230 LOAD_CONST              18 ('JUMP_TARGET')
+            232 LOAD_CONST              13 ('label')
+            234 LOAD_CONST              19 (12)
+            236 BUILD_MAP                1
+            238 LOAD_CONST              20 (11)
+            240 LOAD_CONST               4 (1)
+            242 LOAD_CONST               5 (False)
+            244 CALL_FUNCTION            6
             246 POP_TOP
+            248 EXTENDED_ARG             1
+            250 FOR_ITER               354 (to 606)
+            252 BUILD_LIST               1
+            254 DUP_TOP
+            256 LOAD_GLOBAL              0 (py_instrument_receiver)
+            258 ROT_TWO
+            260 LOAD_CONST               2 (125)
+            262 LOAD_CONST              21 ('i')
+            264 LOAD_CONST              22 (13)
+            266 LOAD_CONST               4 (1)
+            268 LOAD_CONST               5 (False)
+            270 CALL_FUNCTION            6
             272 POP_TOP
             274 UNPACK_SEQUENCE          1
+            276 STORE_FAST               2 (i)
+  6         278 LOAD_FAST                2 (i)
+            280 BUILD_LIST               1
+            282 DUP_TOP
+            284 LOAD_GLOBAL              0 (py_instrument_receiver)
+            286 ROT_TWO
+            288 LOAD_CONST              16 (124)
+            290 LOAD_CONST              21 ('i')
+            292 LOAD_CONST              23 (14)
+            294 LOAD_CONST               4 (1)
+            296 LOAD_CONST               8 (True)
+            298 CALL_FUNCTION            6
             300 POP_TOP
             302 UNPACK_SEQUENCE          1
             304 LOAD_CONST              24 (3)
             306 COMPARE_OP               2 (==)
             308 EXTENDED_ARG             1
+            310 POP_JUMP_IF_FALSE      316
+  7         312 BREAK_LOOP
+            314 JUMP_ABSOLUTE          226
+  9     >>  316 LOAD_GLOBAL              0 (py_instrument_receiver)
+            318 BUILD_LIST               0
+            320 LOAD_CONST              18 ('JUMP_TARGET')
+            322 LOAD_CONST              13 ('label')
+            324 LOAD_CONST              25 (21)
+            326 BUILD_MAP                1
+            328 LOAD_CONST              26 (20)
+            330 LOAD_CONST               4 (1)
+            332 LOAD_CONST               5 (False)
+            334 CALL_FUNCTION            6
+            336 POP_TOP
+            338 LOAD_GLOBAL              0 (py_instrument_receiver)
+            340 BUILD_LIST               0
+            342 LOAD_CONST              12 (120)
+            344 LOAD_CONST              13 ('label')
+            346 LOAD_CONST              27 (39)
+            348 BUILD_MAP                1
+            350 LOAD_CONST              25 (21)
+            352 LOAD_CONST               4 (1)
             354 LOAD_CONST               5 (False)
+            356 CALL_FUNCTION            6
+            358 POP_TOP
+            360 SETUP_LOOP             220 (to 582)
+        >>  362 LOAD_GLOBAL              0 (py_instrument_receiver)
+            364 BUILD_LIST               0
+            366 LOAD_CONST              18 ('JUMP_TARGET')
+            368 LOAD_CONST              13 ('label')
+            370 LOAD_CONST              28 (23)
+            372 BUILD_MAP                1
+            374 LOAD_CONST              29 (22)
+            376 LOAD_CONST               4 (1)
             378 LOAD_CONST               5 (False)
+            380 CALL_FUNCTION            6
+            382 POP_TOP
+            384 LOAD_FAST                2 (i)
+            386 BUILD_LIST               1
+            388 DUP_TOP
+            390 LOAD_GLOBAL              0 (py_instrument_receiver)
+            392 ROT_TWO
+            394 LOAD_CONST              16 (124)
+            396 LOAD_CONST              21 ('i')
+            398 LOAD_CONST              28 (23)
+            400 LOAD_CONST               4 (1)
+            402 LOAD_CONST               8 (True)
             404 CALL_FUNCTION            6
             406 POP_TOP
             408 UNPACK_SEQUENCE          1
             410 LOAD_CONST              30 (0)
+            412 COMPARE_OP               4 (>)
+            414 EXTENDED_ARG             2
+            416 POP_JUMP_IF_FALSE      558
+ 10         418 LOAD_FAST                0 (x)
+            420 BUILD_LIST               1
+            422 DUP_TOP
+            424 LOAD_GLOBAL              0 (py_instrument_receiver)
+            426 ROT_TWO
+            428 LOAD_CONST              16 (124)
+            430 LOAD_CONST               3 ('x')
+            432 LOAD_CONST              31 (27)
+            434 LOAD_CONST               4 (1)
             436 LOAD_CONST               8 (True)
+            438 CALL_FUNCTION            6
+            440 POP_TOP
+            442 UNPACK_SEQUENCE          1
+            444 LOAD_FAST                2 (i)
+            446 BUILD_LIST               1
+            448 DUP_TOP
+            450 LOAD_GLOBAL              0 (py_instrument_receiver)
+            452 ROT_TWO
+            454 LOAD_CONST              16 (124)
+            456 LOAD_CONST              21 ('i')
+            458 LOAD_CONST              32 (28)
+            460 LOAD_CONST               4 (1)
             462 LOAD_CONST               8 (True)
+            464 CALL_FUNCTION            6
+            466 POP_TOP
+            468 UNPACK_SEQUENCE          1
+            470 INPLACE_ADD
+            472 BUILD_LIST               1
+            474 DUP_TOP
+            476 LOAD_GLOBAL              0 (py_instrument_receiver)
+            478 ROT_TWO
+            480 LOAD_CONST               2 (125)
+            482 LOAD_CONST               3 ('x')
+            484 LOAD_CONST              33 (30)
+            486 LOAD_CONST               4 (1)
             488 LOAD_CONST               5 (False)
             490 CALL_FUNCTION            6
+            492 POP_TOP
+            494 UNPACK_SEQUENCE          1
+            496 STORE_FAST               0 (x)
+ 11         498 LOAD_FAST                2 (i)
+            500 BUILD_LIST               1
+            502 DUP_TOP
+            504 LOAD_GLOBAL              0 (py_instrument_receiver)
+            506 ROT_TWO
+            508 LOAD_CONST              16 (124)
+            510 LOAD_CONST              21 ('i')
+            512 LOAD_CONST              34 (31)
+            514 LOAD_CONST               4 (1)
             516 LOAD_CONST               8 (True)
             518 CALL_FUNCTION            6
+            520 POP_TOP
+            522 UNPACK_SEQUENCE          1
+            524 LOAD_CONST               4 (1)
+            526 INPLACE_SUBTRACT
+            528 BUILD_LIST               1
+            530 DUP_TOP
+            532 LOAD_GLOBAL              0 (py_instrument_receiver)
+            534 ROT_TWO
+            536 LOAD_CONST               2 (125)
+            538 LOAD_CONST              21 ('i')
+            540 LOAD_CONST              35 (34)
+            542 LOAD_CONST               4 (1)
             544 LOAD_CONST               5 (False)
             546 CALL_FUNCTION            6
+            548 POP_TOP
+            550 UNPACK_SEQUENCE          1
+            552 STORE_FAST               2 (i)
+            554 EXTENDED_ARG             1
+            556 JUMP_ABSOLUTE          362
+        >>  558 LOAD_GLOBAL              0 (py_instrument_receiver)
+            560 BUILD_LIST               0
+            562 LOAD_CONST              18 ('JUMP_TARGET')
+            564 LOAD_CONST              13 ('label')
+            566 LOAD_CONST              36 (37)
+            568 BUILD_MAP                1
             570 LOAD_CONST              37 (36)
+            572 LOAD_CONST               4 (1)
+            574 LOAD_CONST               5 (False)
+            576 CALL_FUNCTION            6
+            578 POP_TOP
+            580 POP_BLOCK
+        >>  582 LOAD_GLOBAL              0 (py_instrument_receiver)
+            584 BUILD_LIST               0
+            586 LOAD_CONST              18 ('JUMP_TARGET')
+            588 LOAD_CONST              13 ('label')
+            590 LOAD_CONST              27 (39)
+            592 BUILD_MAP                1
             594 LOAD_CONST              38 (38)
+            596 LOAD_CONST               4 (1)
+            598 LOAD_CONST               5 (False)
+            600 CALL_FUNCTION            6
+            602 POP_TOP
+            604 JUMP_ABSOLUTE          226
+        >>  606 LOAD_GLOBAL              0 (py_instrument_receiver)
+            608 BUILD_LIST               0
+            610 LOAD_CONST              18 ('JUMP_TARGET')
+            612 LOAD_CONST              13 ('label')
+            614 LOAD_CONST              39 (41)
+            616 BUILD_MAP                1
             618 LOAD_CONST              40 (40)
+            620 LOAD_CONST               4 (1)
+            622 LOAD_CONST               5 (False)
+            624 CALL_FUNCTION            6
+            626 POP_TOP
+            628 POP_BLOCK
+        >>  630 LOAD_GLOBAL              0 (py_instrument_receiver)
+            632 BUILD_LIST               0
+            634 LOAD_CONST              18 ('JUMP_TARGET')
+            636 LOAD_CONST              13 ('label')
+            638 LOAD_CONST              14 (43)
+            640 BUILD_MAP                1
             642 LOAD_CONST              41 (42)
             644 LOAD_CONST               4 (1)
'''

snapshots['test_nested_iteration (2, 3, 7)'] = [
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 82,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 26,
        'stack': [
            -1
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 64,
        'stack': [
            GenericRepr("<class 'range'>"),
            5
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 64,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 120,
        'stack': [
            GenericRepr("<class 'list'>"),
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 120,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'data',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 170,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': {
            'label': 642
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 194,
        'stack': [
        ]
    },
    {
        'arg': 'data',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 196,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arrive_at': 246
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 272,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 274,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 354
    },
    {
        'arg': {
            'label': 594
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 354,
        'stack': [
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 570
    },
    {
        'arrive_at': 594
    },
    {
        'arrive_at': 246
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 272,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 274,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 354
    },
    {
        'arg': {
            'label': 594
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 354,
        'stack': [
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 410,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 436,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 488,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 490,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 544,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 570
    },
    {
        'arrive_at': 594
    },
    {
        'arrive_at': 246
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 272,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 274,
        'stack': [
            2
        ]
    },
    {
        'arrive_at': 354
    },
    {
        'arg': {
            'label': 594
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 354,
        'stack': [
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            2
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 410,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 436,
        'stack': [
            2
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 488,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 490,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 544,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 410,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 436,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 488,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 490,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 544,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 378
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 378,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 570
    },
    {
        'arrive_at': 594
    },
    {
        'arrive_at': 246
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 272,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 274,
        'stack': [
            3
        ]
    },
    {
        'arrive_at': 642
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

snapshots['test_factorial (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object factorial at SOME ADDRESS, file "<string>", line 2>)
               2 LOAD_CONST               1 ('factorial')
               4 MAKE_FUNCTION            0
+              6 BUILD_LIST               1
+              8 DUP_TOP
+             10 LOAD_GLOBAL              0 (py_instrument_receiver)
+             12 ROT_TWO
+             14 LOAD_CONST               2 (90)
+             16 LOAD_CONST               1 ('factorial')
+             18 LOAD_CONST               3 (3)
+             20 LOAD_CONST               4 (0)
+             22 LOAD_CONST               5 (False)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 STORE_NAME               1 (factorial)
   8          32 LOAD_NAME                1 (factorial)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               6 (101)
+             44 LOAD_CONST               1 ('factorial')
+             46 LOAD_CONST               7 (4)
+             48 LOAD_CONST               4 (0)
+             50 LOAD_CONST               8 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
              58 LOAD_CONST               9 (5)
+             60 BUILD_LIST               2
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST              10 (131)
+             70 LOAD_CONST              11 (1)
+             72 LOAD_CONST              12 (6)
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
+            102 LOAD_CONST              11 (1)
+            104 LOAD_CONST              12 (6)
+            106 LOAD_CONST               4 (0)
+            108 LOAD_CONST               8 (True)
+            110 CALL_FUNCTION            6
+            112 POP_TOP
+            114 UNPACK_SEQUENCE          1
             116 POP_TOP
             118 LOAD_CONST              13 (None)
             120 RETURN_VALUE

Code Object: factorial
   3           0 LOAD_FAST                0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (124)
+             12 LOAD_CONST               2 ('i')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               3 (0)
              28 COMPARE_OP               2 (==)
              30 POP_JUMP_IF_FALSE       36
   4          32 LOAD_CONST               4 (1)
              34 RETURN_VALUE
+  6     >>   36 LOAD_GLOBAL              0 (py_instrument_receiver)
+             38 BUILD_LIST               0
+             40 LOAD_CONST               6 ('JUMP_TARGET')
+             42 LOAD_CONST               7 ('label')
+             44 LOAD_CONST               8 (7)
+             46 BUILD_MAP                1
+             48 LOAD_CONST               9 (6)
+             50 LOAD_CONST               4 (1)
+             52 LOAD_CONST              10 (False)
+             54 CALL_FUNCTION            6
+             56 POP_TOP
              58 LOAD_FAST                0 (i)
+             60 BUILD_LIST               1
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST               1 (124)
+             70 LOAD_CONST               2 ('i')
+             72 LOAD_CONST               8 (7)
+             74 LOAD_CONST               4 (1)
+             76 LOAD_CONST               5 (True)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 UNPACK_SEQUENCE          1
              84 LOAD_GLOBAL              1 (factorial)
              86 LOAD_FAST                0 (i)
+             88 BUILD_LIST               1
+             90 DUP_TOP
+             92 LOAD_GLOBAL              0 (py_instrument_receiver)
+             94 ROT_TWO
+             96 LOAD_CONST               1 (124)
+             98 LOAD_CONST               2 ('i')
+            100 LOAD_CONST              11 (9)
+            102 LOAD_CONST               4 (1)
+            104 LOAD_CONST               5 (True)
+            106 CALL_FUNCTION            6
+            108 POP_TOP
+            110 UNPACK_SEQUENCE          1
             112 LOAD_CONST               4 (1)
             114 BINARY_SUBTRACT
+            116 BUILD_LIST               2
+            118 DUP_TOP
+            120 LOAD_GLOBAL              0 (py_instrument_receiver)
+            122 ROT_TWO
+            124 LOAD_CONST              12 (131)
+            126 LOAD_CONST               4 (1)
+            128 LOAD_CONST              13 (12)
+            130 LOAD_CONST               4 (1)
+            132 LOAD_CONST              10 (False)
+            134 CALL_FUNCTION            6
+            136 POP_TOP
+            138 LOAD_GLOBAL              2 (reversed)
+            140 ROT_TWO
+            142 CALL_FUNCTION            1
+            144 UNPACK_SEQUENCE          2
             146 CALL_FUNCTION            1
+            148 BUILD_LIST               1
+            150 DUP_TOP
+            152 LOAD_GLOBAL              0 (py_instrument_receiver)
+            154 ROT_TWO
+            156 LOAD_CONST              12 (131)
+            158 LOAD_CONST               4 (1)
+            160 LOAD_CONST              13 (12)
+            162 LOAD_CONST               4 (1)
+            164 LOAD_CONST               5 (True)
+            166 CALL_FUNCTION            6
+            168 POP_TOP
+            170 UNPACK_SEQUENCE          1
             172 BINARY_MULTIPLY
             174 RETURN_VALUE
             176 LOAD_CONST               0 (None)
             178 RETURN_VALUE
'''

snapshots['test_factorial (2, 3, 7)'] = [
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            5
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            5
        ]
    },
    {
        'arrive_at': 58
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 58,
        'stack': [
            5
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 86,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            4
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            4
        ]
    },
    {
        'arrive_at': 58
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 58,
        'stack': [
            4
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 86,
        'stack': [
            4
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            3
        ]
    },
    {
        'arrive_at': 58
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 58,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 86,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            2
        ]
    },
    {
        'arrive_at': 58
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 58,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 86,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 58
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 58,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 86,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            0
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            6
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 146,
        'stack': [
            24
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            120
        ]
    }
]

snapshots['test_list_map (1, 3, 7)'] = '''
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
+             18 LOAD_CONST               4 ('my_arr')
+             20 LOAD_CONST               5 (4)
+             22 LOAD_CONST               6 (0)
+             24 LOAD_CONST               7 (False)
+             26 CALL_FUNCTION            6
+             28 POP_TOP
+             30 UNPACK_SEQUENCE          1
              32 STORE_NAME               1 (my_arr)
+  3          34 LOAD_GLOBAL              0 (py_instrument_receiver)
+             36 BUILD_LIST               0
+             38 LOAD_CONST               8 (120)
+             40 LOAD_CONST               9 ('label')
+             42 LOAD_CONST              10 (26)
+             44 BUILD_MAP                1
+             46 LOAD_CONST              11 (5)
+             48 LOAD_CONST               6 (0)
+             50 LOAD_CONST               7 (False)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
              56 EXTENDED_ARG             1
              58 SETUP_LOOP             360 (to 420)
+             60 LOAD_NAME                2 (range)
+             62 BUILD_LIST               1
+             64 DUP_TOP
+             66 LOAD_GLOBAL              0 (py_instrument_receiver)
+             68 ROT_TWO
+             70 LOAD_CONST              12 (101)
+             72 LOAD_CONST              13 ('range')
+             74 LOAD_CONST              14 (6)
+             76 LOAD_CONST               6 (0)
+             78 LOAD_CONST              15 (True)
+             80 CALL_FUNCTION            6
+             82 POP_TOP
              84 UNPACK_SEQUENCE          1
              86 LOAD_CONST               6 (0)
+             88 LOAD_CONST               2 (3)
+             90 BUILD_LIST               3
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST              16 (131)
+            100 LOAD_CONST               1 (2)
+            102 LOAD_CONST              17 (9)
+            104 LOAD_CONST               6 (0)
+            106 LOAD_CONST               7 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 LOAD_GLOBAL              3 (reversed)
+            114 ROT_TWO
+            116 CALL_FUNCTION            1
             118 UNPACK_SEQUENCE          3
+            120 CALL_FUNCTION            2
+            122 BUILD_LIST               1
+            124 DUP_TOP
+            126 LOAD_GLOBAL              0 (py_instrument_receiver)
+            128 ROT_TWO
+            130 LOAD_CONST              16 (131)
+            132 LOAD_CONST               1 (2)
+            134 LOAD_CONST              17 (9)
+            136 LOAD_CONST               6 (0)
+            138 LOAD_CONST              15 (True)
+            140 CALL_FUNCTION            6
+            142 POP_TOP
             144 UNPACK_SEQUENCE          1
+            146 GET_ITER
+        >>  148 LOAD_GLOBAL              0 (py_instrument_receiver)
+            150 BUILD_LIST               0
+            152 LOAD_CONST              18 ('JUMP_TARGET')
+            154 LOAD_CONST               9 ('label')
+            156 LOAD_CONST              19 (12)
+            158 BUILD_MAP                1
+            160 LOAD_CONST              20 (11)
+            162 LOAD_CONST               6 (0)
+            164 LOAD_CONST               7 (False)
+            166 CALL_FUNCTION            6
             168 POP_TOP
+            170 FOR_ITER               224 (to 396)
+            172 BUILD_LIST               1
+            174 DUP_TOP
+            176 LOAD_GLOBAL              0 (py_instrument_receiver)
+            178 ROT_TWO
+            180 LOAD_CONST               3 (90)
+            182 LOAD_CONST              21 ('i')
+            184 LOAD_CONST              22 (13)
+            186 LOAD_CONST               6 (0)
+            188 LOAD_CONST               7 (False)
+            190 CALL_FUNCTION            6
+            192 POP_TOP
             194 UNPACK_SEQUENCE          1
             196 STORE_NAME               4 (i)
+  4         198 LOAD_NAME                1 (my_arr)
+            200 BUILD_LIST               1
+            202 DUP_TOP
+            204 LOAD_GLOBAL              0 (py_instrument_receiver)
+            206 ROT_TWO
+            208 LOAD_CONST              12 (101)
+            210 LOAD_CONST               4 ('my_arr')
+            212 LOAD_CONST              23 (14)
+            214 LOAD_CONST               6 (0)
+            216 LOAD_CONST              15 (True)
+            218 CALL_FUNCTION            6
+            220 POP_TOP
             222 UNPACK_SEQUENCE          1
+            224 LOAD_NAME                4 (i)
+            226 BUILD_LIST               1
+            228 DUP_TOP
+            230 LOAD_GLOBAL              0 (py_instrument_receiver)
+            232 ROT_TWO
+            234 LOAD_CONST              12 (101)
+            236 LOAD_CONST              21 ('i')
+            238 LOAD_CONST              24 (15)
+            240 LOAD_CONST               6 (0)
+            242 LOAD_CONST              15 (True)
+            244 CALL_FUNCTION            6
+            246 POP_TOP
+            248 UNPACK_SEQUENCE          1
+            250 BUILD_LIST               2
+            252 DUP_TOP
+            254 LOAD_GLOBAL              0 (py_instrument_receiver)
+            256 ROT_TWO
+            258 LOAD_CONST              25 (25)
+            260 LOAD_CONST              26 (None)
+            262 LOAD_CONST              27 (16)
+            264 LOAD_CONST               6 (0)
+            266 LOAD_CONST               7 (False)
+            268 CALL_FUNCTION            6
+            270 POP_TOP
+            272 LOAD_GLOBAL              3 (reversed)
+            274 ROT_TWO
+            276 CALL_FUNCTION            1
             278 UNPACK_SEQUENCE          2
+            280 BINARY_SUBSCR
+            282 BUILD_LIST               1
+            284 DUP_TOP
+            286 LOAD_GLOBAL              0 (py_instrument_receiver)
+            288 ROT_TWO
+            290 LOAD_CONST              25 (25)
+            292 LOAD_CONST              26 (None)
+            294 LOAD_CONST              27 (16)
+            296 LOAD_CONST               6 (0)
+            298 LOAD_CONST              15 (True)
+            300 CALL_FUNCTION            6
+            302 POP_TOP
             304 UNPACK_SEQUENCE          1
             306 LOAD_CONST               0 (1)
             308 BINARY_ADD
+            310 LOAD_NAME                1 (my_arr)
+            312 BUILD_LIST               1
+            314 DUP_TOP
+            316 LOAD_GLOBAL              0 (py_instrument_receiver)
+            318 ROT_TWO
+            320 LOAD_CONST              12 (101)
+            322 LOAD_CONST               4 ('my_arr')
+            324 LOAD_CONST              28 (19)
+            326 LOAD_CONST               6 (0)
+            328 LOAD_CONST              15 (True)
+            330 CALL_FUNCTION            6
+            332 POP_TOP
             334 UNPACK_SEQUENCE          1
+            336 LOAD_NAME                4 (i)
+            338 BUILD_LIST               1
+            340 DUP_TOP
+            342 LOAD_GLOBAL              0 (py_instrument_receiver)
+            344 ROT_TWO
+            346 LOAD_CONST              12 (101)
+            348 LOAD_CONST              21 ('i')
+            350 LOAD_CONST              29 (20)
+            352 LOAD_CONST               6 (0)
+            354 LOAD_CONST              15 (True)
+            356 CALL_FUNCTION            6
+            358 POP_TOP
+            360 UNPACK_SEQUENCE          1
+            362 BUILD_LIST               3
+            364 DUP_TOP
+            366 LOAD_GLOBAL              0 (py_instrument_receiver)
+            368 ROT_TWO
+            370 LOAD_CONST              30 (60)
+            372 LOAD_CONST              26 (None)
+            374 LOAD_CONST              31 (21)
+            376 LOAD_CONST               6 (0)
+            378 LOAD_CONST               7 (False)
+            380 CALL_FUNCTION            6
+            382 POP_TOP
+            384 LOAD_GLOBAL              3 (reversed)
+            386 ROT_TWO
+            388 CALL_FUNCTION            1
             390 UNPACK_SEQUENCE          3
             392 STORE_SUBSCR
+            394 JUMP_ABSOLUTE          148
+        >>  396 LOAD_GLOBAL              0 (py_instrument_receiver)
+            398 BUILD_LIST               0
+            400 LOAD_CONST              18 ('JUMP_TARGET')
+            402 LOAD_CONST               9 ('label')
+            404 LOAD_CONST              32 (24)
+            406 BUILD_MAP                1
+            408 LOAD_CONST              33 (23)
+            410 LOAD_CONST               6 (0)
+            412 LOAD_CONST               7 (False)
+            414 CALL_FUNCTION            6
             416 POP_TOP
+            418 POP_BLOCK
+        >>  420 LOAD_GLOBAL              0 (py_instrument_receiver)
+            422 BUILD_LIST               0
+            424 LOAD_CONST              18 ('JUMP_TARGET')
+            426 LOAD_CONST               9 ('label')
+            428 LOAD_CONST              10 (26)
+            430 BUILD_MAP                1
+            432 LOAD_CONST              25 (25)
+            434 LOAD_CONST               6 (0)
+            436 LOAD_CONST               7 (False)
+            438 CALL_FUNCTION            6
             440 POP_TOP
             442 LOAD_CONST              26 (None)
'''

snapshots['test_list_map (2, 3, 7)'] = [
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 32,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': {
            'label': 440
        },
        'code': '<module>',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 56,
        'stack': [
        ]
    },
    {
        'arg': 'range',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 58,
        'stack': [
            GenericRepr("<class 'range'>")
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 118,
        'stack': [
            GenericRepr("<class 'range'>"),
            0,
            3
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 118,
        'stack': [
            GenericRepr('range(0, 3)')
        ]
    },
    {
        'arrive_at': 168
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 194,
        'stack': [
            0
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 196,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 222,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            [
                2,
                3,
                4
            ],
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            1
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 308,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 334,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 390,
        'stack': [
            2,
            [
                2,
                3,
                4
            ],
            0
        ]
    },
    {
        'arrive_at': 168
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 194,
        'stack': [
            1
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 196,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 222,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            [
                2,
                3,
                4
            ],
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 308,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 334,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 390,
        'stack': [
            3,
            [
                2,
                3,
                4
            ],
            1
        ]
    },
    {
        'arrive_at': 168
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 194,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 196,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 222,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            [
                2,
                3,
                4
            ],
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 278,
        'stack': [
            3
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 308,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 334,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 390,
        'stack': [
            4,
            [
                2,
                3,
                4
            ],
            2
        ]
    },
    {
        'arrive_at': 168
    },
    {
        'arrive_at': 416
    },
    {
        'arrive_at': 440
    }
]

snapshots['test_nonlocal_load (1, 3, 7)'] = '''
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
              58 LOAD_CONST               4 (0)
+             60 BUILD_LIST               2
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST               9 (131)
+             70 LOAD_CONST              10 (1)
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
+            100 LOAD_CONST               9 (131)
+            102 LOAD_CONST              10 (1)
+            104 LOAD_CONST              11 (6)
+            106 LOAD_CONST               4 (0)
+            108 LOAD_CONST               8 (True)
+            110 CALL_FUNCTION            6
+            112 POP_TOP
+            114 UNPACK_SEQUENCE          1
             116 POP_TOP
   8         118 LOAD_NAME                1 (f)
+            120 BUILD_LIST               1
+            122 DUP_TOP
+            124 LOAD_GLOBAL              0 (py_instrument_receiver)
+            126 ROT_TWO
+            128 LOAD_CONST               6 (101)
+            130 LOAD_CONST               1 ('f')
+            132 LOAD_CONST              12 (8)
+            134 LOAD_CONST               4 (0)
+            136 LOAD_CONST               8 (True)
+            138 CALL_FUNCTION            6
+            140 POP_TOP
+            142 UNPACK_SEQUENCE          1
             144 LOAD_CONST              10 (1)
+            146 BUILD_LIST               2
+            148 DUP_TOP
+            150 LOAD_GLOBAL              0 (py_instrument_receiver)
+            152 ROT_TWO
+            154 LOAD_CONST               9 (131)
+            156 LOAD_CONST              10 (1)
+            158 LOAD_CONST              13 (10)
+            160 LOAD_CONST               4 (0)
+            162 LOAD_CONST               5 (False)
+            164 CALL_FUNCTION            6
+            166 POP_TOP
+            168 LOAD_GLOBAL              2 (reversed)
+            170 ROT_TWO
+            172 CALL_FUNCTION            1
+            174 UNPACK_SEQUENCE          2
             176 CALL_FUNCTION            1
+            178 BUILD_LIST               1
+            180 DUP_TOP
+            182 LOAD_GLOBAL              0 (py_instrument_receiver)
+            184 ROT_TWO
+            186 LOAD_CONST               9 (131)
+            188 LOAD_CONST              10 (1)
+            190 LOAD_CONST              13 (10)
+            192 LOAD_CONST               4 (0)
+            194 LOAD_CONST               8 (True)
+            196 CALL_FUNCTION            6
+            198 POP_TOP
+            200 UNPACK_SEQUENCE          1
             202 POP_TOP
             204 LOAD_CONST              14 (None)
             206 RETURN_VALUE

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
              34 LOAD_CONST               8 ('f.<locals>.g')
              36 MAKE_FUNCTION            8
+             38 BUILD_LIST               1
+             40 DUP_TOP
+             42 LOAD_GLOBAL              0 (py_instrument_receiver)
+             44 ROT_TWO
+             46 LOAD_CONST               9 (125)
+             48 LOAD_CONST              10 ('g')
+             50 LOAD_CONST              11 (5)
+             52 LOAD_CONST               5 (1)
+             54 LOAD_CONST              12 (False)
+             56 CALL_FUNCTION            6
+             58 POP_TOP
+             60 UNPACK_SEQUENCE          1
              62 STORE_FAST               1 (g)
   6          64 LOAD_FAST                1 (g)
+             66 BUILD_LIST               1
+             68 DUP_TOP
+             70 LOAD_GLOBAL              0 (py_instrument_receiver)
+             72 ROT_TWO
+             74 LOAD_CONST              13 (124)
+             76 LOAD_CONST              10 ('g')
+             78 LOAD_CONST              14 (6)
+             80 LOAD_CONST               5 (1)
+             82 LOAD_CONST               6 (True)
+             84 CALL_FUNCTION            6
+             86 POP_TOP
+             88 UNPACK_SEQUENCE          1
+             90 BUILD_LIST               1
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST              15 (131)
+            100 LOAD_CONST               4 (0)
+            102 LOAD_CONST              16 (7)
+            104 LOAD_CONST               5 (1)
+            106 LOAD_CONST              12 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
             114 CALL_FUNCTION            0
+            116 BUILD_LIST               1
+            118 DUP_TOP
+            120 LOAD_GLOBAL              0 (py_instrument_receiver)
+            122 ROT_TWO
+            124 LOAD_CONST              15 (131)
+            126 LOAD_CONST               4 (0)
+            128 LOAD_CONST              16 (7)
+            130 LOAD_CONST               5 (1)
+            132 LOAD_CONST               6 (True)
+            134 CALL_FUNCTION            6
+            136 POP_TOP
+            138 UNPACK_SEQUENCE          1
             140 POP_TOP
             142 LOAD_CONST               0 (None)
             144 RETURN_VALUE

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

snapshots['test_nonlocal_load (2, 3, 7)'] = [
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 30,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 32,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 90,
        'stack': [
            '<function f at SOME ADDRESS>',
            0
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
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 64,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 114,
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
            0
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 114,
        'stack': [
            0
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
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 118,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 176,
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
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 62,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 64,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 114,
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
        'orig_op': 176,
        'stack': [
            None
        ]
    }
]

snapshots['test_scope_forwarding_loads (1, 3, 7)'] = '''
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
   3          28 LOAD_CONST               5 (2)
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              0 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               1 (90)
+             40 LOAD_CONST               6 ('y')
+             42 LOAD_CONST               7 (3)
+             44 LOAD_CONST               3 (0)
+             46 LOAD_CONST               4 (False)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 UNPACK_SEQUENCE          1
              54 STORE_NAME               2 (y)
   4          56 LOAD_CONST               7 (3)
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               1 (90)
+             68 LOAD_CONST               8 ('z')
+             70 LOAD_CONST               9 (5)
+             72 LOAD_CONST               3 (0)
+             74 LOAD_CONST               4 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 STORE_NAME               3 (z)
~  5          84 LOAD_CONST              10 (<code object f1 at SOME ADDRESS, file "<string>", line 5>)
              86 LOAD_CONST              11 ('f1')
              88 MAKE_FUNCTION            0
+             90 BUILD_LIST               1
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST               1 (90)
+            100 LOAD_CONST              11 ('f1')
+            102 LOAD_CONST              12 (9)
+            104 LOAD_CONST               3 (0)
+            106 LOAD_CONST               4 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
             114 STORE_NAME               4 (f1)
  19         116 LOAD_NAME                4 (f1)
+            118 BUILD_LIST               1
+            120 DUP_TOP
+            122 LOAD_GLOBAL              0 (py_instrument_receiver)
+            124 ROT_TWO
+            126 LOAD_CONST              13 (101)
+            128 LOAD_CONST              11 ('f1')
+            130 LOAD_CONST              14 (10)
+            132 LOAD_CONST               3 (0)
+            134 LOAD_CONST              15 (True)
+            136 CALL_FUNCTION            6
+            138 POP_TOP
+            140 UNPACK_SEQUENCE          1
+            142 BUILD_LIST               1
+            144 DUP_TOP
+            146 LOAD_GLOBAL              0 (py_instrument_receiver)
+            148 ROT_TWO
+            150 LOAD_CONST              16 (131)
+            152 LOAD_CONST               3 (0)
+            154 LOAD_CONST              17 (11)
+            156 LOAD_CONST               3 (0)
+            158 LOAD_CONST               4 (False)
+            160 CALL_FUNCTION            6
+            162 POP_TOP
+            164 UNPACK_SEQUENCE          1
             166 CALL_FUNCTION            0
+            168 BUILD_LIST               1
+            170 DUP_TOP
+            172 LOAD_GLOBAL              0 (py_instrument_receiver)
+            174 ROT_TWO
+            176 LOAD_CONST              16 (131)
+            178 LOAD_CONST               3 (0)
+            180 LOAD_CONST              17 (11)
+            182 LOAD_CONST               3 (0)
+            184 LOAD_CONST              15 (True)
+            186 CALL_FUNCTION            6
+            188 POP_TOP
+            190 UNPACK_SEQUENCE          1
             192 POP_TOP
             194 LOAD_CONST              18 (None)
             196 RETURN_VALUE

Code Object: f1
   6           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (125)
+             12 LOAD_CONST               2 ('test1')
+             14 LOAD_CONST               3 (1)
+             16 LOAD_CONST               3 (1)
+             18 LOAD_CONST               4 (False)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 STORE_FAST               0 (test1)
   7          28 LOAD_CONST               5 (4)
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              1 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               6 (137)
+             40 LOAD_CONST               7 ('cell')
+             42 LOAD_CONST               8 ('w')
+             44 BUILD_MAP                1
+             46 LOAD_CONST               9 (3)
+             48 LOAD_CONST               3 (1)
+             50 LOAD_CONST               4 (False)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
              58 STORE_DEREF              0 (w)
   8          60 LOAD_CONST              10 (5)
+             62 BUILD_LIST               1
+             64 DUP_TOP
+             66 LOAD_GLOBAL              1 (py_instrument_receiver)
+             68 ROT_TWO
+             70 LOAD_CONST               1 (125)
+             72 LOAD_CONST              11 ('u')
+             74 LOAD_CONST              10 (5)
+             76 LOAD_CONST               3 (1)
+             78 LOAD_CONST               4 (False)
+             80 CALL_FUNCTION            6
+             82 POP_TOP
+             84 UNPACK_SEQUENCE          1
              86 STORE_FAST               1 (u)
   9          88 LOAD_CLOSURE             0 (w)
+             90 BUILD_LIST               1
+             92 DUP_TOP
+             94 LOAD_GLOBAL              1 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST              12 (135)
+            100 LOAD_CONST               7 ('cell')
+            102 LOAD_CONST               8 ('w')
+            104 BUILD_MAP                1
+            106 LOAD_CONST              13 (6)
+            108 LOAD_CONST               3 (1)
+            110 LOAD_CONST              14 (True)
+            112 CALL_FUNCTION            6
+            114 POP_TOP
+            116 UNPACK_SEQUENCE          1
             118 BUILD_TUPLE              1
~            120 LOAD_CONST              15 (<code object f2 at SOME ADDRESS, file "<string>", line 9>)
             122 LOAD_CONST              16 ('f1.<locals>.f2')
             124 MAKE_FUNCTION            8
+            126 BUILD_LIST               1
+            128 DUP_TOP
+            130 LOAD_GLOBAL              1 (py_instrument_receiver)
+            132 ROT_TWO
+            134 LOAD_CONST               1 (125)
+            136 LOAD_CONST              17 ('f2')
+            138 LOAD_CONST              18 (11)
+            140 LOAD_CONST               3 (1)
+            142 LOAD_CONST               4 (False)
+            144 CALL_FUNCTION            6
+            146 POP_TOP
+            148 UNPACK_SEQUENCE          1
             150 STORE_FAST               2 (f2)
  18         152 LOAD_FAST                2 (f2)
+            154 BUILD_LIST               1
+            156 DUP_TOP
+            158 LOAD_GLOBAL              1 (py_instrument_receiver)
+            160 ROT_TWO
+            162 LOAD_CONST              19 (124)
+            164 LOAD_CONST              17 ('f2')
+            166 LOAD_CONST              20 (12)
+            168 LOAD_CONST               3 (1)
+            170 LOAD_CONST              14 (True)
+            172 CALL_FUNCTION            6
+            174 POP_TOP
+            176 UNPACK_SEQUENCE          1
+            178 BUILD_LIST               1
+            180 DUP_TOP
+            182 LOAD_GLOBAL              1 (py_instrument_receiver)
+            184 ROT_TWO
+            186 LOAD_CONST              21 (131)
+            188 LOAD_CONST              22 (0)
+            190 LOAD_CONST              23 (13)
+            192 LOAD_CONST               3 (1)
+            194 LOAD_CONST               4 (False)
+            196 CALL_FUNCTION            6
+            198 POP_TOP
+            200 UNPACK_SEQUENCE          1
             202 CALL_FUNCTION            0
+            204 BUILD_LIST               1
+            206 DUP_TOP
+            208 LOAD_GLOBAL              1 (py_instrument_receiver)
+            210 ROT_TWO
+            212 LOAD_CONST              21 (131)
+            214 LOAD_CONST              22 (0)
+            216 LOAD_CONST              23 (13)
+            218 LOAD_CONST               3 (1)
+            220 LOAD_CONST              14 (True)
+            222 CALL_FUNCTION            6
+            224 POP_TOP
+            226 UNPACK_SEQUENCE          1
             228 POP_TOP
             230 LOAD_CONST               0 (None)
             232 RETURN_VALUE

Code Object: f2
  10           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (125)
+             12 LOAD_CONST               2 ('test2')
+             14 LOAD_CONST               3 (1)
+             16 LOAD_CONST               4 (2)
+             18 LOAD_CONST               5 (False)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 STORE_FAST               0 (test2)
  11          28 LOAD_DEREF               1 (w)
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              1 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               6 (136)
+             40 LOAD_CONST               7 ('free')
+             42 LOAD_CONST               8 ('w')
+             44 BUILD_MAP                1
+             46 LOAD_CONST               4 (2)
+             48 LOAD_CONST               4 (2)
+             50 LOAD_CONST               9 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              1 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               1 (125)
+             68 LOAD_CONST              10 ('test3')
+             70 LOAD_CONST              11 (3)
+             72 LOAD_CONST               4 (2)
+             74 LOAD_CONST               5 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 STORE_FAST               1 (test3)
  12          84 LOAD_CONST              12 (6)
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              1 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST              13 (137)
+             96 LOAD_CONST              14 ('cell')
+             98 LOAD_CONST              15 ('u')
+            100 BUILD_MAP                1
+            102 LOAD_CONST              16 (5)
+            104 LOAD_CONST               4 (2)
+            106 LOAD_CONST               5 (False)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
             114 STORE_DEREF              0 (u)
  13         116 LOAD_CLOSURE             0 (u)
+            118 BUILD_LIST               1
+            120 DUP_TOP
+            122 LOAD_GLOBAL              1 (py_instrument_receiver)
+            124 ROT_TWO
+            126 LOAD_CONST              17 (135)
+            128 LOAD_CONST              14 ('cell')
+            130 LOAD_CONST              15 ('u')
+            132 BUILD_MAP                1
+            134 LOAD_CONST              12 (6)
+            136 LOAD_CONST               4 (2)
+            138 LOAD_CONST               9 (True)
+            140 CALL_FUNCTION            6
+            142 POP_TOP
+            144 UNPACK_SEQUENCE          1
             146 LOAD_CLOSURE             1 (w)
+            148 BUILD_LIST               1
+            150 DUP_TOP
+            152 LOAD_GLOBAL              1 (py_instrument_receiver)
+            154 ROT_TWO
+            156 LOAD_CONST              17 (135)
+            158 LOAD_CONST               7 ('free')
+            160 LOAD_CONST               8 ('w')
+            162 BUILD_MAP                1
+            164 LOAD_CONST              18 (7)
+            166 LOAD_CONST               4 (2)
+            168 LOAD_CONST               9 (True)
+            170 CALL_FUNCTION            6
+            172 POP_TOP
+            174 UNPACK_SEQUENCE          1
             176 BUILD_TUPLE              2
~            178 LOAD_CONST              19 (<code object f3 at SOME ADDRESS, file "<string>", line 13>)
             180 LOAD_CONST              20 ('f1.<locals>.f2.<locals>.f3')
             182 MAKE_FUNCTION            8
+            184 BUILD_LIST               1
+            186 DUP_TOP
+            188 LOAD_GLOBAL              1 (py_instrument_receiver)
+            190 ROT_TWO
+            192 LOAD_CONST               1 (125)
+            194 LOAD_CONST              21 ('f3')
+            196 LOAD_CONST              22 (12)
+            198 LOAD_CONST               4 (2)
+            200 LOAD_CONST               5 (False)
+            202 CALL_FUNCTION            6
+            204 POP_TOP
+            206 UNPACK_SEQUENCE          1
             208 STORE_FAST               2 (f3)
  17         210 LOAD_FAST                2 (f3)
+            212 BUILD_LIST               1
+            214 DUP_TOP
+            216 LOAD_GLOBAL              1 (py_instrument_receiver)
+            218 ROT_TWO
+            220 LOAD_CONST              23 (124)
+            222 LOAD_CONST              21 ('f3')
+            224 LOAD_CONST              24 (13)
+            226 LOAD_CONST               4 (2)
+            228 LOAD_CONST               9 (True)
+            230 CALL_FUNCTION            6
+            232 POP_TOP
+            234 UNPACK_SEQUENCE          1
+            236 BUILD_LIST               1
+            238 DUP_TOP
+            240 LOAD_GLOBAL              1 (py_instrument_receiver)
+            242 ROT_TWO
+            244 LOAD_CONST              25 (131)
+            246 LOAD_CONST              26 (0)
+            248 LOAD_CONST              27 (14)
+            250 LOAD_CONST               4 (2)
+            252 LOAD_CONST               5 (False)
+            254 CALL_FUNCTION            6
+            256 POP_TOP
+            258 UNPACK_SEQUENCE          1
             260 CALL_FUNCTION            0
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              1 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              25 (131)
+            272 LOAD_CONST              26 (0)
+            274 LOAD_CONST              27 (14)
+            276 LOAD_CONST               4 (2)
+            278 LOAD_CONST               9 (True)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 POP_TOP
             288 LOAD_CONST               0 (None)
             290 RETURN_VALUE

Code Object: f3
  14           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (125)
+             12 LOAD_CONST               2 ('test4')
+             14 LOAD_CONST               3 (1)
+             16 LOAD_CONST               4 (3)
+             18 LOAD_CONST               5 (False)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 STORE_FAST               0 (test4)
  15          28 LOAD_DEREF               1 (w)
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              1 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               6 (136)
+             40 LOAD_CONST               7 ('free')
+             42 LOAD_CONST               8 ('w')
+             44 BUILD_MAP                1
+             46 LOAD_CONST               9 (2)
+             48 LOAD_CONST               4 (3)
+             50 LOAD_CONST              10 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              1 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               1 (125)
+             68 LOAD_CONST              11 ('test5')
+             70 LOAD_CONST               4 (3)
+             72 LOAD_CONST               4 (3)
+             74 LOAD_CONST               5 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 STORE_FAST               1 (test5)
  16          84 LOAD_DEREF               0 (u)
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              1 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST               6 (136)
+             96 LOAD_CONST               7 ('free')
+             98 LOAD_CONST              12 ('u')
+            100 BUILD_MAP                1
+            102 LOAD_CONST              13 (4)
+            104 LOAD_CONST               4 (3)
+            106 LOAD_CONST              10 (True)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
+            114 BUILD_LIST               1
+            116 DUP_TOP
+            118 LOAD_GLOBAL              1 (py_instrument_receiver)
+            120 ROT_TWO
+            122 LOAD_CONST               1 (125)
+            124 LOAD_CONST              14 ('test6')
+            126 LOAD_CONST              15 (5)
+            128 LOAD_CONST               4 (3)
+            130 LOAD_CONST               5 (False)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
             138 STORE_FAST               2 (test6)
             140 LOAD_CONST               0 (None)
             142 RETURN_VALUE
'''

snapshots['test_scope_forwarding_loads (2, 3, 7)'] = [
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
        'arg': 'y',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 54,
        'stack': [
            2
        ]
    },
    {
        'arg': 'z',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 82,
        'stack': [
            3
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 114,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 116,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 166,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'test1',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 26,
        'stack': [
            1
        ]
    },
    {
        'arg': {
            'cell': 'w'
        },
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 58,
        'stack': [
            4
        ]
    },
    {
        'arg': 'u',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 86,
        'stack': [
            5
        ]
    },
    {
        'arg': {
            'cell': 'w'
        },
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 88,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 150,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 152,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 202,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'test2',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 26,
        'stack': [
            1
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 28,
        'stack': [
            4
        ]
    },
    {
        'arg': 'test3',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 82,
        'stack': [
            4
        ]
    },
    {
        'arg': {
            'cell': 'u'
        },
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 114,
        'stack': [
            6
        ]
    },
    {
        'arg': {
            'cell': 'u'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 116,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 146,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 208,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 210,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 260,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'test4',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 26,
        'stack': [
            1
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 28,
        'stack': [
            4
        ]
    },
    {
        'arg': 'test5',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 82,
        'stack': [
            4
        ]
    },
    {
        'arg': {
            'free': 'u'
        },
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 84,
        'stack': [
            6
        ]
    },
    {
        'arg': 'test6',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 138,
        'stack': [
            6
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 260,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 202,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 166,
        'stack': [
            None
        ]
    }
]
