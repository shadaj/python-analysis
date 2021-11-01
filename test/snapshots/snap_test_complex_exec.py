# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_nested_iteration (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object myFunc at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object myFunc at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('myFunc')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('myFunc')
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
+             64 LOAD_CONST               4 ('myFunc')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (myFunc)
  12          80 LOAD_NAME                1 (myFunc)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('myFunc')
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

Code Object: myFunc
   3           0 LOAD_CONST               1 (-1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (100)
+             12 LOAD_CONST               1 (-1)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (125)
+             36 LOAD_CONST               7 ('x')
+             38 LOAD_CONST               4 (1)
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               8 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_FAST               0 (x)
   4          52 LOAD_GLOBAL              1 (list)
              54 LOAD_GLOBAL              2 (range)
              56 LOAD_CONST               9 (5)
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               2 (100)
+             68 LOAD_CONST               9 (5)
+             70 LOAD_CONST              10 (4)
+             72 LOAD_CONST               4 (1)
+             74 LOAD_CONST               5 (True)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
+             82 BUILD_LIST               2
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST              11 (131)
+             92 LOAD_CONST               4 (1)
+             94 LOAD_CONST               9 (5)
+             96 LOAD_CONST               4 (1)
+             98 LOAD_CONST               8 (False)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 LOAD_GLOBAL              3 (reversed)
+            106 ROT_TWO
+            108 CALL_FUNCTION            1
+            110 UNPACK_SEQUENCE          2
             112 CALL_FUNCTION            1
+            114 BUILD_LIST               1
+            116 DUP_TOP
+            118 LOAD_GLOBAL              0 (py_instrument_receiver)
+            120 ROT_TWO
+            122 LOAD_CONST              11 (131)
+            124 LOAD_CONST               4 (1)
+            126 LOAD_CONST               9 (5)
+            128 LOAD_CONST               4 (1)
+            130 LOAD_CONST               5 (True)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
+            138 BUILD_LIST               2
+            140 DUP_TOP
+            142 LOAD_GLOBAL              0 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST              11 (131)
+            148 LOAD_CONST               4 (1)
+            150 LOAD_CONST              12 (6)
+            152 LOAD_CONST               4 (1)
+            154 LOAD_CONST               8 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 LOAD_GLOBAL              3 (reversed)
+            162 ROT_TWO
+            164 CALL_FUNCTION            1
+            166 UNPACK_SEQUENCE          2
             168 CALL_FUNCTION            1
+            170 BUILD_LIST               1
+            172 DUP_TOP
+            174 LOAD_GLOBAL              0 (py_instrument_receiver)
+            176 ROT_TWO
+            178 LOAD_CONST              11 (131)
+            180 LOAD_CONST               4 (1)
+            182 LOAD_CONST              12 (6)
+            184 LOAD_CONST               4 (1)
+            186 LOAD_CONST               5 (True)
+            188 CALL_FUNCTION            6
+            190 POP_TOP
+            192 UNPACK_SEQUENCE          1
+            194 BUILD_LIST               1
+            196 DUP_TOP
+            198 LOAD_GLOBAL              0 (py_instrument_receiver)
+            200 ROT_TWO
+            202 LOAD_CONST               6 (125)
+            204 LOAD_CONST              13 ('data')
+            206 LOAD_CONST              14 (7)
+            208 LOAD_CONST               4 (1)
+            210 LOAD_CONST               8 (False)
+            212 CALL_FUNCTION            6
+            214 POP_TOP
+            216 UNPACK_SEQUENCE          1
             218 STORE_FAST               1 (data)
+  5         220 LOAD_GLOBAL              0 (py_instrument_receiver)
+            222 BUILD_LIST               0
+            224 LOAD_CONST              15 (120)
+            226 LOAD_CONST              16 ('label')
+            228 LOAD_CONST              17 (43)
+            230 BUILD_MAP                1
+            232 LOAD_CONST              18 (8)
+            234 LOAD_CONST               4 (1)
+            236 LOAD_CONST               8 (False)
+            238 CALL_FUNCTION            6
+            240 POP_TOP
             242 EXTENDED_ARG             3
             244 SETUP_LOOP             782 (to 1028)
+            246 LOAD_FAST                1 (data)
+            248 BUILD_LIST               1
+            250 DUP_TOP
+            252 LOAD_GLOBAL              0 (py_instrument_receiver)
+            254 ROT_TWO
+            256 LOAD_CONST              19 (124)
+            258 LOAD_CONST              13 ('data')
+            260 LOAD_CONST              20 (9)
+            262 LOAD_CONST               4 (1)
+            264 LOAD_CONST               5 (True)
+            266 CALL_FUNCTION            6
+            268 POP_TOP
             270 UNPACK_SEQUENCE          1
+            272 GET_ITER
+        >>  274 LOAD_GLOBAL              0 (py_instrument_receiver)
+            276 BUILD_LIST               0
+            278 LOAD_CONST              21 ('JUMP_TARGET')
+            280 LOAD_CONST              16 ('label')
+            282 LOAD_CONST              22 (12)
+            284 BUILD_MAP                1
+            286 LOAD_CONST              23 (11)
+            288 LOAD_CONST               4 (1)
+            290 LOAD_CONST               8 (False)
+            292 CALL_FUNCTION            6
             294 POP_TOP
+            296 EXTENDED_ARG             2
+            298 FOR_ITER               704 (to 1004)
+            300 BUILD_LIST               1
+            302 DUP_TOP
+            304 LOAD_GLOBAL              0 (py_instrument_receiver)
+            306 ROT_TWO
+            308 LOAD_CONST               6 (125)
+            310 LOAD_CONST              24 ('i')
+            312 LOAD_CONST              25 (13)
+            314 LOAD_CONST               4 (1)
+            316 LOAD_CONST               8 (False)
+            318 CALL_FUNCTION            6
             320 POP_TOP
             322 UNPACK_SEQUENCE          1
+            324 STORE_FAST               2 (i)
+  6         326 LOAD_FAST                2 (i)
+            328 BUILD_LIST               1
+            330 DUP_TOP
+            332 LOAD_GLOBAL              0 (py_instrument_receiver)
+            334 ROT_TWO
+            336 LOAD_CONST              19 (124)
+            338 LOAD_CONST              24 ('i')
+            340 LOAD_CONST              26 (14)
+            342 LOAD_CONST               4 (1)
+            344 LOAD_CONST               5 (True)
+            346 CALL_FUNCTION            6
             348 POP_TOP
+            350 UNPACK_SEQUENCE          1
+            352 LOAD_CONST              27 (3)
+            354 BUILD_LIST               1
+            356 DUP_TOP
+            358 LOAD_GLOBAL              0 (py_instrument_receiver)
+            360 ROT_TWO
+            362 LOAD_CONST               2 (100)
+            364 LOAD_CONST              27 (3)
+            366 LOAD_CONST              28 (15)
+            368 LOAD_CONST               4 (1)
+            370 LOAD_CONST               5 (True)
+            372 CALL_FUNCTION            6
+            374 POP_TOP
+            376 UNPACK_SEQUENCE          1
+            378 BUILD_LIST               2
+            380 DUP_TOP
+            382 LOAD_GLOBAL              0 (py_instrument_receiver)
+            384 ROT_TWO
+            386 LOAD_CONST              29 (107)
+            388 LOAD_CONST              30 (<Compare.EQ: 2>)
+            390 LOAD_CONST              31 (16)
+            392 LOAD_CONST               4 (1)
+            394 LOAD_CONST               8 (False)
+            396 CALL_FUNCTION            6
+            398 POP_TOP
+            400 LOAD_GLOBAL              3 (reversed)
+            402 ROT_TWO
             404 CALL_FUNCTION            1
+            406 UNPACK_SEQUENCE          2
+            408 COMPARE_OP               2 (==)
+            410 BUILD_LIST               1
+            412 DUP_TOP
+            414 LOAD_GLOBAL              0 (py_instrument_receiver)
+            416 ROT_TWO
+            418 LOAD_CONST              29 (107)
+            420 LOAD_CONST              30 (<Compare.EQ: 2>)
+            422 LOAD_CONST              31 (16)
+            424 LOAD_CONST               4 (1)
+            426 LOAD_CONST               5 (True)
+            428 CALL_FUNCTION            6
+            430 POP_TOP
+            432 UNPACK_SEQUENCE          1
+            434 BUILD_LIST               1
+            436 DUP_TOP
+            438 LOAD_GLOBAL              0 (py_instrument_receiver)
+            440 ROT_TWO
+            442 LOAD_CONST              32 (114)
+            444 LOAD_CONST              16 ('label')
+            446 LOAD_CONST              33 (21)
+            448 BUILD_MAP                1
+            450 LOAD_CONST              34 (17)
+            452 LOAD_CONST               4 (1)
+            454 LOAD_CONST               8 (False)
+            456 CALL_FUNCTION            6
             458 POP_TOP
             460 UNPACK_SEQUENCE          1
             462 EXTENDED_ARG             1
+            464 POP_JUMP_IF_FALSE      472
+  7         466 BREAK_LOOP
+            468 EXTENDED_ARG             1
+            470 JUMP_ABSOLUTE          274
+  9     >>  472 LOAD_GLOBAL              0 (py_instrument_receiver)
+            474 BUILD_LIST               0
+            476 LOAD_CONST              21 ('JUMP_TARGET')
+            478 LOAD_CONST              16 ('label')
+            480 LOAD_CONST              33 (21)
+            482 BUILD_MAP                1
+            484 LOAD_CONST              35 (20)
+            486 LOAD_CONST               4 (1)
+            488 LOAD_CONST               8 (False)
+            490 CALL_FUNCTION            6
+            492 POP_TOP
+            494 LOAD_GLOBAL              0 (py_instrument_receiver)
+            496 BUILD_LIST               0
+            498 LOAD_CONST              15 (120)
+            500 LOAD_CONST              16 ('label')
+            502 LOAD_CONST              36 (39)
+            504 BUILD_MAP                1
+            506 LOAD_CONST              33 (21)
             508 LOAD_CONST               4 (1)
+            510 LOAD_CONST               8 (False)
+            512 CALL_FUNCTION            6
+            514 POP_TOP
+            516 EXTENDED_ARG             1
+            518 SETUP_LOOP             458 (to 978)
+        >>  520 LOAD_GLOBAL              0 (py_instrument_receiver)
+            522 BUILD_LIST               0
+            524 LOAD_CONST              21 ('JUMP_TARGET')
+            526 LOAD_CONST              16 ('label')
+            528 LOAD_CONST              37 (23)
+            530 BUILD_MAP                1
             532 LOAD_CONST              38 (22)
+            534 LOAD_CONST               4 (1)
+            536 LOAD_CONST               8 (False)
+            538 CALL_FUNCTION            6
+            540 POP_TOP
+            542 LOAD_FAST                2 (i)
+            544 BUILD_LIST               1
+            546 DUP_TOP
+            548 LOAD_GLOBAL              0 (py_instrument_receiver)
+            550 ROT_TWO
+            552 LOAD_CONST              19 (124)
+            554 LOAD_CONST              24 ('i')
+            556 LOAD_CONST              37 (23)
             558 LOAD_CONST               4 (1)
+            560 LOAD_CONST               5 (True)
+            562 CALL_FUNCTION            6
+            564 POP_TOP
+            566 UNPACK_SEQUENCE          1
+            568 LOAD_CONST               3 (0)
+            570 BUILD_LIST               1
+            572 DUP_TOP
+            574 LOAD_GLOBAL              0 (py_instrument_receiver)
+            576 ROT_TWO
+            578 LOAD_CONST               2 (100)
+            580 LOAD_CONST               3 (0)
+            582 LOAD_CONST              39 (24)
+            584 LOAD_CONST               4 (1)
+            586 LOAD_CONST               5 (True)
+            588 CALL_FUNCTION            6
+            590 POP_TOP
+            592 UNPACK_SEQUENCE          1
+            594 BUILD_LIST               2
+            596 DUP_TOP
+            598 LOAD_GLOBAL              0 (py_instrument_receiver)
+            600 ROT_TWO
+            602 LOAD_CONST              29 (107)
+            604 LOAD_CONST              40 (<Compare.GT: 4>)
+            606 LOAD_CONST              41 (25)
+            608 LOAD_CONST               4 (1)
+            610 LOAD_CONST               8 (False)
+            612 CALL_FUNCTION            6
             614 POP_TOP
+            616 LOAD_GLOBAL              3 (reversed)
+            618 ROT_TWO
+            620 CALL_FUNCTION            1
+            622 UNPACK_SEQUENCE          2
+            624 COMPARE_OP               4 (>)
+            626 BUILD_LIST               1
+            628 DUP_TOP
+            630 LOAD_GLOBAL              0 (py_instrument_receiver)
+            632 ROT_TWO
+            634 LOAD_CONST              29 (107)
+            636 LOAD_CONST              40 (<Compare.GT: 4>)
+            638 LOAD_CONST              41 (25)
+            640 LOAD_CONST               4 (1)
+            642 LOAD_CONST               5 (True)
+            644 CALL_FUNCTION            6
+            646 POP_TOP
+            648 UNPACK_SEQUENCE          1
+            650 BUILD_LIST               1
+            652 DUP_TOP
+            654 LOAD_GLOBAL              0 (py_instrument_receiver)
+            656 ROT_TWO
+            658 LOAD_CONST              32 (114)
+            660 LOAD_CONST              16 ('label')
+            662 LOAD_CONST              42 (37)
+            664 BUILD_MAP                1
+            666 LOAD_CONST              43 (26)
             668 LOAD_CONST               4 (1)
             670 LOAD_CONST               8 (False)
+            672 CALL_FUNCTION            6
+            674 POP_TOP
+            676 UNPACK_SEQUENCE          1
+            678 EXTENDED_ARG             3
+            680 POP_JUMP_IF_FALSE      954
+ 10         682 LOAD_FAST                0 (x)
+            684 BUILD_LIST               1
+            686 DUP_TOP
+            688 LOAD_GLOBAL              0 (py_instrument_receiver)
+            690 ROT_TWO
+            692 LOAD_CONST              19 (124)
+            694 LOAD_CONST               7 ('x')
             696 LOAD_CONST              44 (27)
+            698 LOAD_CONST               4 (1)
+            700 LOAD_CONST               5 (True)
+            702 CALL_FUNCTION            6
+            704 POP_TOP
+            706 UNPACK_SEQUENCE          1
+            708 LOAD_FAST                2 (i)
+            710 BUILD_LIST               1
+            712 DUP_TOP
+            714 LOAD_GLOBAL              0 (py_instrument_receiver)
+            716 ROT_TWO
+            718 LOAD_CONST              19 (124)
+            720 LOAD_CONST              24 ('i')
+            722 LOAD_CONST              45 (28)
+            724 LOAD_CONST               4 (1)
+            726 LOAD_CONST               5 (True)
+            728 CALL_FUNCTION            6
+            730 POP_TOP
+            732 UNPACK_SEQUENCE          1
+            734 BUILD_LIST               2
+            736 DUP_TOP
+            738 LOAD_GLOBAL              0 (py_instrument_receiver)
+            740 ROT_TWO
+            742 LOAD_CONST              46 (55)
+            744 LOAD_CONST               0 (None)
+            746 LOAD_CONST              47 (29)
+            748 LOAD_CONST               4 (1)
+            750 LOAD_CONST               8 (False)
             752 CALL_FUNCTION            6
+            754 POP_TOP
+            756 LOAD_GLOBAL              3 (reversed)
+            758 ROT_TWO
+            760 CALL_FUNCTION            1
+            762 UNPACK_SEQUENCE          2
+            764 INPLACE_ADD
+            766 BUILD_LIST               1
+            768 DUP_TOP
+            770 LOAD_GLOBAL              0 (py_instrument_receiver)
+            772 ROT_TWO
+            774 LOAD_CONST              46 (55)
+            776 LOAD_CONST               0 (None)
+            778 LOAD_CONST              47 (29)
+            780 LOAD_CONST               4 (1)
+            782 LOAD_CONST               5 (True)
+            784 CALL_FUNCTION            6
+            786 POP_TOP
+            788 UNPACK_SEQUENCE          1
+            790 BUILD_LIST               1
+            792 DUP_TOP
+            794 LOAD_GLOBAL              0 (py_instrument_receiver)
+            796 ROT_TWO
+            798 LOAD_CONST               6 (125)
+            800 LOAD_CONST               7 ('x')
             802 LOAD_CONST              48 (30)
             804 LOAD_CONST               4 (1)
+            806 LOAD_CONST               8 (False)
+            808 CALL_FUNCTION            6
+            810 POP_TOP
+            812 UNPACK_SEQUENCE          1
+            814 STORE_FAST               0 (x)
+ 11         816 LOAD_FAST                2 (i)
+            818 BUILD_LIST               1
+            820 DUP_TOP
+            822 LOAD_GLOBAL              0 (py_instrument_receiver)
+            824 ROT_TWO
+            826 LOAD_CONST              19 (124)
+            828 LOAD_CONST              24 ('i')
             830 LOAD_CONST              49 (31)
+            832 LOAD_CONST               4 (1)
+            834 LOAD_CONST               5 (True)
+            836 CALL_FUNCTION            6
+            838 POP_TOP
+            840 UNPACK_SEQUENCE          1
+            842 LOAD_CONST               4 (1)
+            844 BUILD_LIST               1
+            846 DUP_TOP
+            848 LOAD_GLOBAL              0 (py_instrument_receiver)
+            850 ROT_TWO
+            852 LOAD_CONST               2 (100)
+            854 LOAD_CONST               4 (1)
+            856 LOAD_CONST              50 (32)
+            858 LOAD_CONST               4 (1)
+            860 LOAD_CONST               5 (True)
+            862 CALL_FUNCTION            6
+            864 POP_TOP
+            866 UNPACK_SEQUENCE          1
+            868 BUILD_LIST               2
+            870 DUP_TOP
+            872 LOAD_GLOBAL              0 (py_instrument_receiver)
+            874 ROT_TWO
+            876 LOAD_CONST              51 (56)
+            878 LOAD_CONST               0 (None)
+            880 LOAD_CONST              52 (33)
+            882 LOAD_CONST               4 (1)
+            884 LOAD_CONST               8 (False)
             886 CALL_FUNCTION            6
+            888 POP_TOP
+            890 LOAD_GLOBAL              3 (reversed)
+            892 ROT_TWO
+            894 CALL_FUNCTION            1
+            896 UNPACK_SEQUENCE          2
+            898 INPLACE_SUBTRACT
+            900 BUILD_LIST               1
+            902 DUP_TOP
+            904 LOAD_GLOBAL              0 (py_instrument_receiver)
+            906 ROT_TWO
+            908 LOAD_CONST              51 (56)
+            910 LOAD_CONST               0 (None)
+            912 LOAD_CONST              52 (33)
+            914 LOAD_CONST               4 (1)
+            916 LOAD_CONST               5 (True)
+            918 CALL_FUNCTION            6
+            920 POP_TOP
+            922 UNPACK_SEQUENCE          1
+            924 BUILD_LIST               1
+            926 DUP_TOP
+            928 LOAD_GLOBAL              0 (py_instrument_receiver)
+            930 ROT_TWO
+            932 LOAD_CONST               6 (125)
+            934 LOAD_CONST              24 ('i')
             936 LOAD_CONST              53 (34)
             938 LOAD_CONST               4 (1)
+            940 LOAD_CONST               8 (False)
+            942 CALL_FUNCTION            6
+            944 POP_TOP
+            946 UNPACK_SEQUENCE          1
+            948 STORE_FAST               2 (i)
+            950 EXTENDED_ARG             2
+            952 JUMP_ABSOLUTE          520
+        >>  954 LOAD_GLOBAL              0 (py_instrument_receiver)
+            956 BUILD_LIST               0
+            958 LOAD_CONST              21 ('JUMP_TARGET')
+            960 LOAD_CONST              16 ('label')
             962 LOAD_CONST              42 (37)
+            964 BUILD_MAP                1
+            966 LOAD_CONST              54 (36)
+            968 LOAD_CONST               4 (1)
+            970 LOAD_CONST               8 (False)
+            972 CALL_FUNCTION            6
+            974 POP_TOP
+            976 POP_BLOCK
+        >>  978 LOAD_GLOBAL              0 (py_instrument_receiver)
+            980 BUILD_LIST               0
+            982 LOAD_CONST              21 ('JUMP_TARGET')
+            984 LOAD_CONST              16 ('label')
             986 LOAD_CONST              36 (39)
+            988 BUILD_MAP                1
+            990 LOAD_CONST              55 (38)
+            992 LOAD_CONST               4 (1)
+            994 LOAD_CONST               8 (False)
+            996 CALL_FUNCTION            6
+            998 POP_TOP
+           1000 EXTENDED_ARG             1
+           1002 JUMP_ABSOLUTE          274
+        >> 1004 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1006 BUILD_LIST               0
+           1008 LOAD_CONST              21 ('JUMP_TARGET')
            1010 LOAD_CONST              16 ('label')
+           1012 LOAD_CONST              56 (41)
+           1014 BUILD_MAP                1
+           1016 LOAD_CONST              57 (40)
+           1018 LOAD_CONST               4 (1)
+           1020 LOAD_CONST               8 (False)
+           1022 CALL_FUNCTION            6
+           1024 POP_TOP
+           1026 POP_BLOCK
+        >> 1028 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1030 BUILD_LIST               0
+           1032 LOAD_CONST              21 ('JUMP_TARGET')
            1034 LOAD_CONST              16 ('label')
+           1036 LOAD_CONST              17 (43)
+           1038 BUILD_MAP                1
+           1040 LOAD_CONST              58 (42)
+           1042 LOAD_CONST               4 (1)
+           1044 LOAD_CONST               8 (False)
+           1046 CALL_FUNCTION            6
+           1048 POP_TOP
+           1050 LOAD_CONST               0 (None)
+           1052 BUILD_LIST               1
+           1054 DUP_TOP
+           1056 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1058 ROT_TWO
            1060 LOAD_CONST               2 (100)
'''

snapshots['test_nested_iteration (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object myFunc at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object myFunc at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'myFunc'
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 130,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': -1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 50,
        'stack': [
            -1
        ]
    },
    {
        'arg': 5,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 56,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 112,
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
        'orig_op': 112,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 168,
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
        'orig_op': 168,
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
        'orig_op': 218,
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
            'label': 1034
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 242,
        'stack': [
        ]
    },
    {
        'arg': 'data',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 244,
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
        'arrive_at': 294
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 320,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 322,
        'stack': [
            0
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 348,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            0,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 508
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 458,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 508
    },
    {
        'arg': {
            'label': 986
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 508,
        'stack': [
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 962
    },
    {
        'arrive_at': 986
    },
    {
        'arrive_at': 294
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 320,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 322,
        'stack': [
            1
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 348,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            1,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 508
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 458,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 508
    },
    {
        'arg': {
            'label': 986
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 508,
        'stack': [
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 670,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 696,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            -1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            0
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 802,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 804,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 830,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 936,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 962
    },
    {
        'arrive_at': 986
    },
    {
        'arrive_at': 294
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 320,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 322,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 348,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            2,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 508
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 458,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 508
    },
    {
        'arg': {
            'label': 986
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 508,
        'stack': [
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            2
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            2,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 670,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 696,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            0,
            2
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            2
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 802,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 804,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 830,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 936,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 670,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 696,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 752,
        'stack': [
            3
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 802,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 804,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 830,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 886,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 936,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 532
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 532,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 558,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 614,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 962
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 668,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 962
    },
    {
        'arrive_at': 986
    },
    {
        'arrive_at': 294
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 320,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 322,
        'stack': [
            3
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 348,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            3,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 404,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 508
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 458,
        'stack': [
            True
        ]
    },
    {
        'arrive_at': 1034
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 1034,
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

snapshots['test_factorial (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object factorial at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object factorial at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('factorial')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('factorial')
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
+             64 LOAD_CONST               4 ('factorial')
+             66 LOAD_CONST               7 (3)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               8 (False)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 STORE_NAME               1 (factorial)
   8          80 LOAD_NAME                1 (factorial)
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              0 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               9 (101)
+             92 LOAD_CONST               4 ('factorial')
+             94 LOAD_CONST              10 (4)
+             96 LOAD_CONST               2 (0)
+             98 LOAD_CONST               3 (True)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 LOAD_CONST              11 (5)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               1 (100)
+            118 LOAD_CONST              11 (5)
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
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               6 (100)
+             38 LOAD_CONST               3 (0)
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               4 (1)
+             44 LOAD_CONST               5 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               7 (107)
+             62 LOAD_CONST               8 (<Compare.EQ: 2>)
+             64 LOAD_CONST               9 (2)
+             66 LOAD_CONST               4 (1)
+             68 LOAD_CONST              10 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 COMPARE_OP               2 (==)
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               7 (107)
+             94 LOAD_CONST               8 (<Compare.EQ: 2>)
+             96 LOAD_CONST               9 (2)
+             98 LOAD_CONST               4 (1)
+            100 LOAD_CONST               5 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST              11 (114)
+            118 LOAD_CONST              12 ('label')
+            120 LOAD_CONST              13 (7)
+            122 BUILD_MAP                1
+            124 LOAD_CONST              14 (3)
+            126 LOAD_CONST               4 (1)
+            128 LOAD_CONST              10 (False)
+            130 CALL_FUNCTION            6
+            132 POP_TOP
+            134 UNPACK_SEQUENCE          1
             136 POP_JUMP_IF_FALSE      166
   4         138 LOAD_CONST               4 (1)
+            140 BUILD_LIST               1
+            142 DUP_TOP
+            144 LOAD_GLOBAL              0 (py_instrument_receiver)
+            146 ROT_TWO
+            148 LOAD_CONST               6 (100)
+            150 LOAD_CONST               4 (1)
+            152 LOAD_CONST              15 (4)
+            154 LOAD_CONST               4 (1)
+            156 LOAD_CONST               5 (True)
+            158 CALL_FUNCTION            6
+            160 POP_TOP
+            162 UNPACK_SEQUENCE          1
             164 RETURN_VALUE
+  6     >>  166 LOAD_GLOBAL              0 (py_instrument_receiver)
+            168 BUILD_LIST               0
+            170 LOAD_CONST              16 ('JUMP_TARGET')
+            172 LOAD_CONST              12 ('label')
+            174 LOAD_CONST              13 (7)
+            176 BUILD_MAP                1
+            178 LOAD_CONST              17 (6)
+            180 LOAD_CONST               4 (1)
+            182 LOAD_CONST              10 (False)
+            184 CALL_FUNCTION            6
+            186 POP_TOP
             188 LOAD_FAST                0 (i)
+            190 BUILD_LIST               1
+            192 DUP_TOP
+            194 LOAD_GLOBAL              0 (py_instrument_receiver)
+            196 ROT_TWO
+            198 LOAD_CONST               1 (124)
+            200 LOAD_CONST               2 ('i')
+            202 LOAD_CONST              13 (7)
+            204 LOAD_CONST               4 (1)
+            206 LOAD_CONST               5 (True)
+            208 CALL_FUNCTION            6
+            210 POP_TOP
+            212 UNPACK_SEQUENCE          1
             214 LOAD_GLOBAL              2 (factorial)
             216 LOAD_FAST                0 (i)
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST               1 (124)
+            228 LOAD_CONST               2 ('i')
+            230 LOAD_CONST              18 (9)
+            232 LOAD_CONST               4 (1)
+            234 LOAD_CONST               5 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
             242 LOAD_CONST               4 (1)
+            244 BUILD_LIST               1
+            246 DUP_TOP
+            248 LOAD_GLOBAL              0 (py_instrument_receiver)
+            250 ROT_TWO
+            252 LOAD_CONST               6 (100)
+            254 LOAD_CONST               4 (1)
+            256 LOAD_CONST              19 (10)
+            258 LOAD_CONST               4 (1)
+            260 LOAD_CONST               5 (True)
+            262 CALL_FUNCTION            6
+            264 POP_TOP
+            266 UNPACK_SEQUENCE          1
+            268 BUILD_LIST               2
+            270 DUP_TOP
+            272 LOAD_GLOBAL              0 (py_instrument_receiver)
+            274 ROT_TWO
+            276 LOAD_CONST              20 (24)
+            278 LOAD_CONST               0 (None)
+            280 LOAD_CONST              21 (11)
+            282 LOAD_CONST               4 (1)
+            284 LOAD_CONST              10 (False)
+            286 CALL_FUNCTION            6
+            288 POP_TOP
+            290 LOAD_GLOBAL              1 (reversed)
+            292 ROT_TWO
+            294 CALL_FUNCTION            1
+            296 UNPACK_SEQUENCE          2
             298 BINARY_SUBTRACT
+            300 BUILD_LIST               1
+            302 DUP_TOP
+            304 LOAD_GLOBAL              0 (py_instrument_receiver)
+            306 ROT_TWO
+            308 LOAD_CONST              20 (24)
+            310 LOAD_CONST               0 (None)
+            312 LOAD_CONST              21 (11)
+            314 LOAD_CONST               4 (1)
+            316 LOAD_CONST               5 (True)
+            318 CALL_FUNCTION            6
+            320 POP_TOP
+            322 UNPACK_SEQUENCE          1
+            324 BUILD_LIST               2
+            326 DUP_TOP
+            328 LOAD_GLOBAL              0 (py_instrument_receiver)
+            330 ROT_TWO
+            332 LOAD_CONST              22 (131)
+            334 LOAD_CONST               4 (1)
+            336 LOAD_CONST              23 (12)
+            338 LOAD_CONST               4 (1)
+            340 LOAD_CONST              10 (False)
+            342 CALL_FUNCTION            6
+            344 POP_TOP
+            346 LOAD_GLOBAL              1 (reversed)
+            348 ROT_TWO
+            350 CALL_FUNCTION            1
+            352 UNPACK_SEQUENCE          2
             354 CALL_FUNCTION            1
+            356 BUILD_LIST               1
+            358 DUP_TOP
+            360 LOAD_GLOBAL              0 (py_instrument_receiver)
+            362 ROT_TWO
+            364 LOAD_CONST              22 (131)
+            366 LOAD_CONST               4 (1)
+            368 LOAD_CONST              23 (12)
+            370 LOAD_CONST               4 (1)
+            372 LOAD_CONST               5 (True)
+            374 CALL_FUNCTION            6
+            376 POP_TOP
+            378 UNPACK_SEQUENCE          1
+            380 BUILD_LIST               2
+            382 DUP_TOP
+            384 LOAD_GLOBAL              0 (py_instrument_receiver)
+            386 ROT_TWO
+            388 LOAD_CONST              24 (20)
+            390 LOAD_CONST               0 (None)
+            392 LOAD_CONST              25 (13)
+            394 LOAD_CONST               4 (1)
+            396 LOAD_CONST              10 (False)
+            398 CALL_FUNCTION            6
+            400 POP_TOP
+            402 LOAD_GLOBAL              1 (reversed)
+            404 ROT_TWO
+            406 CALL_FUNCTION            1
+            408 UNPACK_SEQUENCE          2
             410 BINARY_MULTIPLY
+            412 BUILD_LIST               1
+            414 DUP_TOP
+            416 LOAD_GLOBAL              0 (py_instrument_receiver)
+            418 ROT_TWO
+            420 LOAD_CONST              24 (20)
+            422 LOAD_CONST               0 (None)
+            424 LOAD_CONST              25 (13)
+            426 LOAD_CONST               4 (1)
+            428 LOAD_CONST               5 (True)
+            430 CALL_FUNCTION            6
+            432 POP_TOP
+            434 UNPACK_SEQUENCE          1
             436 RETURN_VALUE
             438 LOAD_CONST               0 (None)
+            440 BUILD_LIST               1
+            442 DUP_TOP
+            444 LOAD_GLOBAL              0 (py_instrument_receiver)
+            446 ROT_TWO
+            448 LOAD_CONST               6 (100)
+            450 LOAD_CONST               0 (None)
+            452 LOAD_CONST              26 (15)
+            454 LOAD_CONST               4 (1)
+            456 LOAD_CONST               5 (True)
+            458 CALL_FUNCTION            6
+            460 POP_TOP
+            462 UNPACK_SEQUENCE          1
             464 RETURN_VALUE
'''

snapshots['test_factorial (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object factorial at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object factorial at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'factorial'
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 78,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 80,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 5,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 106,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            5,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 188
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 188,
        'stack': [
            5
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 216,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 242,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            5,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            4
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            4,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 188
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 188,
        'stack': [
            4
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 216,
        'stack': [
            4
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 242,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            4,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            3,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 188
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 188,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 216,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 242,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            3,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            2,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 188
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 188,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 216,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 242,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 188
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 188,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 216,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 242,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 298,
        'stack': [
            0
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
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
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 188
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            True
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 138,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            3,
            2
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            6
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
        'stack': [
            6
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            4,
            6
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            24
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 354,
        'stack': [
            24
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            5,
            24
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 410,
        'stack': [
            120
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            120
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

snapshots['test_list_map (1, 3, 7)'] = '''
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
+             90 LOAD_CONST               7 ('my_arr')
+             92 LOAD_CONST               8 (4)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               9 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 UNPACK_SEQUENCE          1
             104 STORE_NAME               1 (my_arr)
+  3         106 LOAD_GLOBAL              0 (py_instrument_receiver)
+            108 BUILD_LIST               0
+            110 LOAD_CONST              10 (120)
+            112 LOAD_CONST              11 ('label')
+            114 LOAD_CONST              12 (26)
+            116 BUILD_MAP                1
+            118 LOAD_CONST              13 (5)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               9 (False)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
             128 EXTENDED_ARG             1
             130 SETUP_LOOP             490 (to 622)
+            132 LOAD_NAME                2 (range)
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              0 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST              14 (101)
+            144 LOAD_CONST              15 ('range')
+            146 LOAD_CONST              16 (6)
+            148 LOAD_CONST               2 (0)
+            150 LOAD_CONST               3 (True)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
             156 UNPACK_SEQUENCE          1
+            158 LOAD_CONST               2 (0)
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST               1 (100)
+            170 LOAD_CONST               2 (0)
+            172 LOAD_CONST              17 (7)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               3 (True)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
             182 UNPACK_SEQUENCE          1
+            184 LOAD_CONST               5 (3)
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST               1 (100)
+            196 LOAD_CONST               5 (3)
+            198 LOAD_CONST              18 (8)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               3
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST              19 (131)
+            220 LOAD_CONST               4 (2)
+            222 LOAD_CONST              20 (9)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               9 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 LOAD_GLOBAL              3 (reversed)
+            234 ROT_TWO
+            236 CALL_FUNCTION            1
             238 UNPACK_SEQUENCE          3
+            240 CALL_FUNCTION            2
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST              19 (131)
+            252 LOAD_CONST               4 (2)
+            254 LOAD_CONST              20 (9)
+            256 LOAD_CONST               2 (0)
+            258 LOAD_CONST               3 (True)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
             264 UNPACK_SEQUENCE          1
+            266 GET_ITER
+        >>  268 LOAD_GLOBAL              0 (py_instrument_receiver)
+            270 BUILD_LIST               0
+            272 LOAD_CONST              21 ('JUMP_TARGET')
+            274 LOAD_CONST              11 ('label')
+            276 LOAD_CONST              22 (12)
+            278 BUILD_MAP                1
+            280 LOAD_CONST              23 (11)
+            282 LOAD_CONST               2 (0)
+            284 LOAD_CONST               9 (False)
+            286 CALL_FUNCTION            6
             288 POP_TOP
+            290 EXTENDED_ARG             1
+            292 FOR_ITER               304 (to 598)
+            294 BUILD_LIST               1
+            296 DUP_TOP
+            298 LOAD_GLOBAL              0 (py_instrument_receiver)
+            300 ROT_TWO
+            302 LOAD_CONST               6 (90)
+            304 LOAD_CONST              24 ('i')
+            306 LOAD_CONST              25 (13)
+            308 LOAD_CONST               2 (0)
+            310 LOAD_CONST               9 (False)
+            312 CALL_FUNCTION            6
             314 POP_TOP
             316 UNPACK_SEQUENCE          1
+            318 STORE_NAME               4 (i)
+  4         320 LOAD_NAME                1 (my_arr)
+            322 BUILD_LIST               1
+            324 DUP_TOP
+            326 LOAD_GLOBAL              0 (py_instrument_receiver)
+            328 ROT_TWO
+            330 LOAD_CONST              14 (101)
+            332 LOAD_CONST               7 ('my_arr')
+            334 LOAD_CONST              26 (14)
+            336 LOAD_CONST               2 (0)
+            338 LOAD_CONST               3 (True)
+            340 CALL_FUNCTION            6
             342 POP_TOP
+            344 UNPACK_SEQUENCE          1
+            346 LOAD_NAME                4 (i)
+            348 BUILD_LIST               1
+            350 DUP_TOP
+            352 LOAD_GLOBAL              0 (py_instrument_receiver)
+            354 ROT_TWO
+            356 LOAD_CONST              14 (101)
+            358 LOAD_CONST              24 ('i')
+            360 LOAD_CONST              27 (15)
+            362 LOAD_CONST               2 (0)
+            364 LOAD_CONST               3 (True)
+            366 CALL_FUNCTION            6
+            368 POP_TOP
+            370 UNPACK_SEQUENCE          1
+            372 BUILD_LIST               2
+            374 DUP_TOP
+            376 LOAD_GLOBAL              0 (py_instrument_receiver)
+            378 ROT_TWO
+            380 LOAD_CONST              28 (25)
+            382 LOAD_CONST              29 (None)
+            384 LOAD_CONST              30 (16)
+            386 LOAD_CONST               2 (0)
+            388 LOAD_CONST               9 (False)
+            390 CALL_FUNCTION            6
+            392 POP_TOP
+            394 LOAD_GLOBAL              3 (reversed)
+            396 ROT_TWO
             398 CALL_FUNCTION            1
+            400 UNPACK_SEQUENCE          2
+            402 BINARY_SUBSCR
+            404 BUILD_LIST               1
+            406 DUP_TOP
+            408 LOAD_GLOBAL              0 (py_instrument_receiver)
+            410 ROT_TWO
+            412 LOAD_CONST              28 (25)
+            414 LOAD_CONST              29 (None)
+            416 LOAD_CONST              30 (16)
+            418 LOAD_CONST               2 (0)
+            420 LOAD_CONST               3 (True)
+            422 CALL_FUNCTION            6
             424 POP_TOP
+            426 UNPACK_SEQUENCE          1
+            428 LOAD_CONST               0 (1)
+            430 BUILD_LIST               1
+            432 DUP_TOP
+            434 LOAD_GLOBAL              0 (py_instrument_receiver)
+            436 ROT_TWO
+            438 LOAD_CONST               1 (100)
+            440 LOAD_CONST               0 (1)
+            442 LOAD_CONST              31 (17)
+            444 LOAD_CONST               2 (0)
+            446 LOAD_CONST               3 (True)
+            448 CALL_FUNCTION            6
+            450 POP_TOP
+            452 UNPACK_SEQUENCE          1
+            454 BUILD_LIST               2
+            456 DUP_TOP
+            458 LOAD_GLOBAL              0 (py_instrument_receiver)
+            460 ROT_TWO
+            462 LOAD_CONST              32 (23)
+            464 LOAD_CONST              29 (None)
+            466 LOAD_CONST              33 (18)
+            468 LOAD_CONST               2 (0)
+            470 LOAD_CONST               9 (False)
+            472 CALL_FUNCTION            6
+            474 POP_TOP
+            476 LOAD_GLOBAL              3 (reversed)
+            478 ROT_TWO
             480 CALL_FUNCTION            1
+            482 UNPACK_SEQUENCE          2
+            484 BINARY_ADD
+            486 BUILD_LIST               1
+            488 DUP_TOP
+            490 LOAD_GLOBAL              0 (py_instrument_receiver)
+            492 ROT_TWO
+            494 LOAD_CONST              32 (23)
+            496 LOAD_CONST              29 (None)
+            498 LOAD_CONST              33 (18)
+            500 LOAD_CONST               2 (0)
+            502 LOAD_CONST               3 (True)
+            504 CALL_FUNCTION            6
             506 POP_TOP
+            508 UNPACK_SEQUENCE          1
+            510 LOAD_NAME                1 (my_arr)
+            512 BUILD_LIST               1
+            514 DUP_TOP
+            516 LOAD_GLOBAL              0 (py_instrument_receiver)
+            518 ROT_TWO
+            520 LOAD_CONST              14 (101)
+            522 LOAD_CONST               7 ('my_arr')
+            524 LOAD_CONST              34 (19)
+            526 LOAD_CONST               2 (0)
+            528 LOAD_CONST               3 (True)
+            530 CALL_FUNCTION            6
             532 POP_TOP
+            534 UNPACK_SEQUENCE          1
+            536 LOAD_NAME                4 (i)
+            538 BUILD_LIST               1
+            540 DUP_TOP
+            542 LOAD_GLOBAL              0 (py_instrument_receiver)
+            544 ROT_TWO
+            546 LOAD_CONST              14 (101)
+            548 LOAD_CONST              24 ('i')
+            550 LOAD_CONST              35 (20)
+            552 LOAD_CONST               2 (0)
+            554 LOAD_CONST               3 (True)
+            556 CALL_FUNCTION            6
+            558 POP_TOP
+            560 UNPACK_SEQUENCE          1
+            562 BUILD_LIST               3
+            564 DUP_TOP
+            566 LOAD_GLOBAL              0 (py_instrument_receiver)
+            568 ROT_TWO
+            570 LOAD_CONST              36 (60)
+            572 LOAD_CONST              29 (None)
+            574 LOAD_CONST              37 (21)
+            576 LOAD_CONST               2 (0)
+            578 LOAD_CONST               9 (False)
+            580 CALL_FUNCTION            6
+            582 POP_TOP
+            584 LOAD_GLOBAL              3 (reversed)
+            586 ROT_TWO
             588 CALL_FUNCTION            1
             590 UNPACK_SEQUENCE          3
+            592 STORE_SUBSCR
+            594 EXTENDED_ARG             1
+            596 JUMP_ABSOLUTE          268
+        >>  598 LOAD_GLOBAL              0 (py_instrument_receiver)
+            600 BUILD_LIST               0
+            602 LOAD_CONST              21 ('JUMP_TARGET')
+            604 LOAD_CONST              11 ('label')
+            606 LOAD_CONST              38 (24)
+            608 BUILD_MAP                1
+            610 LOAD_CONST              32 (23)
+            612 LOAD_CONST               2 (0)
             614 LOAD_CONST               9 (False)
+            616 CALL_FUNCTION            6
+            618 POP_TOP
+            620 POP_BLOCK
+        >>  622 LOAD_GLOBAL              0 (py_instrument_receiver)
+            624 BUILD_LIST               0
+            626 LOAD_CONST              21 ('JUMP_TARGET')
+            628 LOAD_CONST              11 ('label')
+            630 LOAD_CONST              12 (26)
+            632 BUILD_MAP                1
+            634 LOAD_CONST              28 (25)
+            636 LOAD_CONST               2 (0)
             638 LOAD_CONST               9 (False)
+            640 CALL_FUNCTION            6
+            642 POP_TOP
+            644 LOAD_CONST              29 (None)
+            646 BUILD_LIST               1
+            648 DUP_TOP
+            650 LOAD_GLOBAL              0 (py_instrument_receiver)
+            652 ROT_TWO
+            654 LOAD_CONST               1 (100)
+            656 LOAD_CONST              29 (None)
+            658 LOAD_CONST              12 (26)
+            660 LOAD_CONST               2 (0)
+            662 LOAD_CONST               3 (True)
             664 CALL_FUNCTION            6
'''

snapshots['test_list_map (2, 3, 7)'] = [
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
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 104,
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
            'label': 638
        },
        'code': '<module>',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 128,
        'stack': [
        ]
    },
    {
        'arg': 'range',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 130,
        'stack': [
            GenericRepr("<class 'range'>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 156,
        'stack': [
            0
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 182,
        'stack': [
            3
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 238,
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
        'orig_op': 238,
        'stack': [
            GenericRepr('range(0, 3)')
        ]
    },
    {
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            0
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
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
        'orig_op': 342,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
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
        'orig_op': 398,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
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
        'orig_op': 532,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
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
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            1
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
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
        'orig_op': 342,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
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
        'orig_op': 398,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            3
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
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
        'orig_op': 532,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
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
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
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
        'orig_op': 342,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
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
        'orig_op': 398,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            3,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            4
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
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
        'orig_op': 532,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
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
        'arrive_at': 288
    },
    {
        'arrive_at': 614
    },
    {
        'arrive_at': 638
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 638,
        'stack': [
            None
        ]
    }
]

snapshots['test_nonlocal_load (1, 3, 7)'] = '''
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
             106 LOAD_CONST               2 (0)
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               1 (100)
+            118 LOAD_CONST               2 (0)
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
   8         208 LOAD_NAME                1 (f)
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               9 (101)
+            220 LOAD_CONST               4 ('f')
+            222 LOAD_CONST              16 (8)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               3 (True)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 LOAD_CONST               5 (1)
+            236 BUILD_LIST               1
+            238 DUP_TOP
+            240 LOAD_GLOBAL              0 (py_instrument_receiver)
+            242 ROT_TWO
+            244 LOAD_CONST               1 (100)
+            246 LOAD_CONST               5 (1)
+            248 LOAD_CONST              17 (9)
+            250 LOAD_CONST               2 (0)
+            252 LOAD_CONST               3 (True)
+            254 CALL_FUNCTION            6
+            256 POP_TOP
+            258 UNPACK_SEQUENCE          1
+            260 BUILD_LIST               2
+            262 DUP_TOP
+            264 LOAD_GLOBAL              0 (py_instrument_receiver)
+            266 ROT_TWO
+            268 LOAD_CONST              12 (131)
+            270 LOAD_CONST               5 (1)
+            272 LOAD_CONST              18 (10)
+            274 LOAD_CONST               2 (0)
+            276 LOAD_CONST               8 (False)
+            278 CALL_FUNCTION            6
+            280 POP_TOP
+            282 LOAD_GLOBAL              2 (reversed)
+            284 ROT_TWO
+            286 CALL_FUNCTION            1
+            288 UNPACK_SEQUENCE          2
             290 CALL_FUNCTION            1
+            292 BUILD_LIST               1
+            294 DUP_TOP
+            296 LOAD_GLOBAL              0 (py_instrument_receiver)
+            298 ROT_TWO
+            300 LOAD_CONST              12 (131)
+            302 LOAD_CONST               5 (1)
+            304 LOAD_CONST              18 (10)
+            306 LOAD_CONST               2 (0)
+            308 LOAD_CONST               3 (True)
+            310 CALL_FUNCTION            6
+            312 POP_TOP
+            314 UNPACK_SEQUENCE          1
             316 POP_TOP
+            318 LOAD_GLOBAL              0 (py_instrument_receiver)
+            320 BUILD_LIST               0
+            322 LOAD_CONST               5 (1)
+            324 LOAD_CONST              14 (None)
+            326 LOAD_CONST              19 (11)
+            328 LOAD_CONST               2 (0)
+            330 LOAD_CONST               3 (True)
+            332 CALL_FUNCTION            6
+            334 POP_TOP
             336 LOAD_CONST              14 (None)
+            338 BUILD_LIST               1
+            340 DUP_TOP
+            342 LOAD_GLOBAL              0 (py_instrument_receiver)
+            344 ROT_TWO
+            346 LOAD_CONST               1 (100)
+            348 LOAD_CONST              14 (None)
+            350 LOAD_CONST              20 (12)
+            352 LOAD_CONST               2 (0)
+            354 LOAD_CONST               3 (True)
+            356 CALL_FUNCTION            6
+            358 POP_TOP
+            360 UNPACK_SEQUENCE          1
             362 RETURN_VALUE

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

snapshots['test_nonlocal_load (2, 3, 7)'] = [
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
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 106,
        'stack': [
            0
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
            0
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 162,
        'stack': [
            0
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
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 208,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 234,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 290,
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
        'orig_op': 290,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 316,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 336,
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
   3          52 LOAD_CONST               7 (2)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               7 (2)
+             66 LOAD_CONST               7 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               1
+             80 DUP_TOP
+             82 LOAD_GLOBAL              0 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               4 (90)
+             88 LOAD_CONST               8 ('y')
+             90 LOAD_CONST               9 (3)
+             92 LOAD_CONST               2 (0)
+             94 LOAD_CONST               6 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 UNPACK_SEQUENCE          1
             102 STORE_NAME               2 (y)
   4         104 LOAD_CONST               9 (3)
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST               1 (100)
+            116 LOAD_CONST               9 (3)
+            118 LOAD_CONST              10 (4)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               3 (True)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
+            130 BUILD_LIST               1
+            132 DUP_TOP
+            134 LOAD_GLOBAL              0 (py_instrument_receiver)
+            136 ROT_TWO
+            138 LOAD_CONST               4 (90)
+            140 LOAD_CONST              11 ('z')
+            142 LOAD_CONST              12 (5)
+            144 LOAD_CONST               2 (0)
+            146 LOAD_CONST               6 (False)
+            148 CALL_FUNCTION            6
+            150 POP_TOP
+            152 UNPACK_SEQUENCE          1
             154 STORE_NAME               3 (z)
~  5         156 LOAD_CONST              13 (<code object f1 at SOME ADDRESS, file "<string>", line 5>)
+            158 BUILD_LIST               1
+            160 DUP_TOP
+            162 LOAD_GLOBAL              0 (py_instrument_receiver)
+            164 ROT_TWO
+            166 LOAD_CONST               1 (100)
+            168 LOAD_CONST              13 (<code object f1 at SOME ADDRESS, file "<string>", line 5>)
+            170 LOAD_CONST              14 (6)
+            172 LOAD_CONST               2 (0)
+            174 LOAD_CONST               3 (True)
+            176 CALL_FUNCTION            6
+            178 POP_TOP
+            180 UNPACK_SEQUENCE          1
             182 LOAD_CONST              15 ('f1')
+            184 BUILD_LIST               1
+            186 DUP_TOP
+            188 LOAD_GLOBAL              0 (py_instrument_receiver)
+            190 ROT_TWO
+            192 LOAD_CONST               1 (100)
+            194 LOAD_CONST              15 ('f1')
+            196 LOAD_CONST              16 (7)
+            198 LOAD_CONST               2 (0)
+            200 LOAD_CONST               3 (True)
+            202 CALL_FUNCTION            6
+            204 POP_TOP
+            206 UNPACK_SEQUENCE          1
             208 MAKE_FUNCTION            0
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               4 (90)
+            220 LOAD_CONST              15 ('f1')
+            222 LOAD_CONST              17 (9)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               6 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 STORE_NAME               4 (f1)
  19         236 LOAD_NAME                4 (f1)
+            238 BUILD_LIST               1
+            240 DUP_TOP
+            242 LOAD_GLOBAL              0 (py_instrument_receiver)
+            244 ROT_TWO
+            246 LOAD_CONST              18 (101)
+            248 LOAD_CONST              15 ('f1')
+            250 LOAD_CONST              19 (10)
+            252 LOAD_CONST               2 (0)
+            254 LOAD_CONST               3 (True)
+            256 CALL_FUNCTION            6
+            258 POP_TOP
+            260 UNPACK_SEQUENCE          1
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              0 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              20 (131)
+            272 LOAD_CONST               2 (0)
+            274 LOAD_CONST              21 (11)
+            276 LOAD_CONST               2 (0)
+            278 LOAD_CONST               6 (False)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 CALL_FUNCTION            0
+            288 BUILD_LIST               1
+            290 DUP_TOP
+            292 LOAD_GLOBAL              0 (py_instrument_receiver)
+            294 ROT_TWO
+            296 LOAD_CONST              20 (131)
+            298 LOAD_CONST               2 (0)
+            300 LOAD_CONST              21 (11)
+            302 LOAD_CONST               2 (0)
+            304 LOAD_CONST               3 (True)
+            306 CALL_FUNCTION            6
+            308 POP_TOP
+            310 UNPACK_SEQUENCE          1
             312 POP_TOP
+            314 LOAD_GLOBAL              0 (py_instrument_receiver)
+            316 BUILD_LIST               0
+            318 LOAD_CONST               0 (1)
+            320 LOAD_CONST              22 (None)
+            322 LOAD_CONST              23 (12)
+            324 LOAD_CONST               2 (0)
+            326 LOAD_CONST               3 (True)
+            328 CALL_FUNCTION            6
+            330 POP_TOP
             332 LOAD_CONST              22 (None)
+            334 BUILD_LIST               1
+            336 DUP_TOP
+            338 LOAD_GLOBAL              0 (py_instrument_receiver)
+            340 ROT_TWO
+            342 LOAD_CONST               1 (100)
+            344 LOAD_CONST              22 (None)
+            346 LOAD_CONST              24 (13)
+            348 LOAD_CONST               2 (0)
+            350 LOAD_CONST               3 (True)
+            352 CALL_FUNCTION            6
+            354 POP_TOP
+            356 UNPACK_SEQUENCE          1
             358 RETURN_VALUE

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
+             38 LOAD_CONST               6 (100)
+             40 LOAD_CONST               5 (4)
+             42 LOAD_CONST               7 (2)
+             44 LOAD_CONST               3 (1)
+             46 LOAD_CONST               8 (True)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 UNPACK_SEQUENCE          1
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               9 (137)
+             64 LOAD_CONST              10 ('cell')
+             66 LOAD_CONST              11 ('w')
+             68 BUILD_MAP                1
+             70 LOAD_CONST              12 (3)
+             72 LOAD_CONST               3 (1)
+             74 LOAD_CONST               4 (False)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
              82 STORE_DEREF              0 (w)
   8          84 LOAD_CONST              13 (5)
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              1 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST               6 (100)
+             96 LOAD_CONST              13 (5)
+             98 LOAD_CONST               5 (4)
+            100 LOAD_CONST               3 (1)
+            102 LOAD_CONST               8 (True)
+            104 CALL_FUNCTION            6
+            106 POP_TOP
+            108 UNPACK_SEQUENCE          1
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST               1 (125)
+            120 LOAD_CONST              14 ('u')
+            122 LOAD_CONST              13 (5)
+            124 LOAD_CONST               3 (1)
+            126 LOAD_CONST               4 (False)
+            128 CALL_FUNCTION            6
+            130 POP_TOP
+            132 UNPACK_SEQUENCE          1
             134 STORE_FAST               1 (u)
   9         136 LOAD_CLOSURE             0 (w)
+            138 BUILD_LIST               1
+            140 DUP_TOP
+            142 LOAD_GLOBAL              1 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST              15 (135)
+            148 LOAD_CONST              10 ('cell')
+            150 LOAD_CONST              11 ('w')
+            152 BUILD_MAP                1
+            154 LOAD_CONST              16 (6)
+            156 LOAD_CONST               3 (1)
+            158 LOAD_CONST               8 (True)
+            160 CALL_FUNCTION            6
+            162 POP_TOP
+            164 UNPACK_SEQUENCE          1
             166 BUILD_TUPLE              1
~            168 LOAD_CONST              17 (<code object f2 at SOME ADDRESS, file "<string>", line 9>)
+            170 BUILD_LIST               1
+            172 DUP_TOP
+            174 LOAD_GLOBAL              1 (py_instrument_receiver)
+            176 ROT_TWO
+            178 LOAD_CONST               6 (100)
+            180 LOAD_CONST              17 (<code object f2 at SOME ADDRESS, file "<string>", line 9>)
+            182 LOAD_CONST              18 (8)
+            184 LOAD_CONST               3 (1)
+            186 LOAD_CONST               8 (True)
+            188 CALL_FUNCTION            6
+            190 POP_TOP
+            192 UNPACK_SEQUENCE          1
             194 LOAD_CONST              19 ('f1.<locals>.f2')
+            196 BUILD_LIST               1
+            198 DUP_TOP
+            200 LOAD_GLOBAL              1 (py_instrument_receiver)
+            202 ROT_TWO
+            204 LOAD_CONST               6 (100)
+            206 LOAD_CONST              19 ('f1.<locals>.f2')
+            208 LOAD_CONST              20 (9)
+            210 LOAD_CONST               3 (1)
+            212 LOAD_CONST               8 (True)
+            214 CALL_FUNCTION            6
+            216 POP_TOP
+            218 UNPACK_SEQUENCE          1
             220 MAKE_FUNCTION            8
+            222 BUILD_LIST               1
+            224 DUP_TOP
+            226 LOAD_GLOBAL              1 (py_instrument_receiver)
+            228 ROT_TWO
+            230 LOAD_CONST               1 (125)
+            232 LOAD_CONST              21 ('f2')
+            234 LOAD_CONST              22 (11)
+            236 LOAD_CONST               3 (1)
+            238 LOAD_CONST               4 (False)
+            240 CALL_FUNCTION            6
+            242 POP_TOP
+            244 UNPACK_SEQUENCE          1
             246 STORE_FAST               2 (f2)
  18         248 LOAD_FAST                2 (f2)
+            250 BUILD_LIST               1
+            252 DUP_TOP
+            254 LOAD_GLOBAL              1 (py_instrument_receiver)
+            256 ROT_TWO
+            258 LOAD_CONST              23 (124)
+            260 LOAD_CONST              21 ('f2')
+            262 LOAD_CONST              24 (12)
+            264 LOAD_CONST               3 (1)
+            266 LOAD_CONST               8 (True)
+            268 CALL_FUNCTION            6
+            270 POP_TOP
+            272 UNPACK_SEQUENCE          1
+            274 BUILD_LIST               1
+            276 DUP_TOP
+            278 LOAD_GLOBAL              1 (py_instrument_receiver)
+            280 ROT_TWO
+            282 LOAD_CONST              25 (131)
+            284 LOAD_CONST              26 (0)
+            286 LOAD_CONST              27 (13)
+            288 LOAD_CONST               3 (1)
+            290 LOAD_CONST               4 (False)
+            292 CALL_FUNCTION            6
+            294 POP_TOP
+            296 UNPACK_SEQUENCE          1
             298 CALL_FUNCTION            0
+            300 BUILD_LIST               1
+            302 DUP_TOP
+            304 LOAD_GLOBAL              1 (py_instrument_receiver)
+            306 ROT_TWO
+            308 LOAD_CONST              25 (131)
+            310 LOAD_CONST              26 (0)
+            312 LOAD_CONST              27 (13)
+            314 LOAD_CONST               3 (1)
+            316 LOAD_CONST               8 (True)
+            318 CALL_FUNCTION            6
+            320 POP_TOP
+            322 UNPACK_SEQUENCE          1
             324 POP_TOP
+            326 LOAD_GLOBAL              1 (py_instrument_receiver)
+            328 BUILD_LIST               0
+            330 LOAD_CONST               3 (1)
+            332 LOAD_CONST               0 (None)
+            334 LOAD_CONST              28 (14)
+            336 LOAD_CONST               3 (1)
+            338 LOAD_CONST               8 (True)
+            340 CALL_FUNCTION            6
+            342 POP_TOP
             344 LOAD_CONST               0 (None)
+            346 BUILD_LIST               1
+            348 DUP_TOP
+            350 LOAD_GLOBAL              1 (py_instrument_receiver)
+            352 ROT_TWO
+            354 LOAD_CONST               6 (100)
+            356 LOAD_CONST               0 (None)
+            358 LOAD_CONST              29 (15)
+            360 LOAD_CONST               3 (1)
+            362 LOAD_CONST               8 (True)
+            364 CALL_FUNCTION            6
+            366 POP_TOP
+            368 UNPACK_SEQUENCE          1
             370 RETURN_VALUE

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
+             94 LOAD_CONST              13 (100)
+             96 LOAD_CONST              12 (6)
+             98 LOAD_CONST              14 (4)
+            100 LOAD_CONST               4 (2)
+            102 LOAD_CONST               9 (True)
+            104 CALL_FUNCTION            6
+            106 POP_TOP
+            108 UNPACK_SEQUENCE          1
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST              15 (137)
+            120 LOAD_CONST              16 ('cell')
+            122 LOAD_CONST              17 ('u')
+            124 BUILD_MAP                1
+            126 LOAD_CONST              18 (5)
+            128 LOAD_CONST               4 (2)
+            130 LOAD_CONST               5 (False)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
             138 STORE_DEREF              0 (u)
  13         140 LOAD_CLOSURE             0 (u)
+            142 BUILD_LIST               1
+            144 DUP_TOP
+            146 LOAD_GLOBAL              1 (py_instrument_receiver)
+            148 ROT_TWO
+            150 LOAD_CONST              19 (135)
+            152 LOAD_CONST              16 ('cell')
+            154 LOAD_CONST              17 ('u')
+            156 BUILD_MAP                1
+            158 LOAD_CONST              12 (6)
+            160 LOAD_CONST               4 (2)
+            162 LOAD_CONST               9 (True)
+            164 CALL_FUNCTION            6
+            166 POP_TOP
+            168 UNPACK_SEQUENCE          1
             170 LOAD_CLOSURE             1 (w)
+            172 BUILD_LIST               1
+            174 DUP_TOP
+            176 LOAD_GLOBAL              1 (py_instrument_receiver)
+            178 ROT_TWO
+            180 LOAD_CONST              19 (135)
+            182 LOAD_CONST               7 ('free')
+            184 LOAD_CONST               8 ('w')
+            186 BUILD_MAP                1
+            188 LOAD_CONST              20 (7)
+            190 LOAD_CONST               4 (2)
+            192 LOAD_CONST               9 (True)
+            194 CALL_FUNCTION            6
+            196 POP_TOP
+            198 UNPACK_SEQUENCE          1
             200 BUILD_TUPLE              2
~            202 LOAD_CONST              21 (<code object f3 at SOME ADDRESS, file "<string>", line 13>)
+            204 BUILD_LIST               1
+            206 DUP_TOP
+            208 LOAD_GLOBAL              1 (py_instrument_receiver)
+            210 ROT_TWO
+            212 LOAD_CONST              13 (100)
+            214 LOAD_CONST              21 (<code object f3 at SOME ADDRESS, file "<string>", line 13>)
+            216 LOAD_CONST              22 (9)
+            218 LOAD_CONST               4 (2)
+            220 LOAD_CONST               9 (True)
+            222 CALL_FUNCTION            6
+            224 POP_TOP
+            226 UNPACK_SEQUENCE          1
             228 LOAD_CONST              23 ('f1.<locals>.f2.<locals>.f3')
+            230 BUILD_LIST               1
+            232 DUP_TOP
+            234 LOAD_GLOBAL              1 (py_instrument_receiver)
+            236 ROT_TWO
+            238 LOAD_CONST              13 (100)
+            240 LOAD_CONST              23 ('f1.<locals>.f2.<locals>.f3')
+            242 LOAD_CONST              24 (10)
+            244 LOAD_CONST               4 (2)
+            246 LOAD_CONST               9 (True)
+            248 CALL_FUNCTION            6
+            250 POP_TOP
+            252 UNPACK_SEQUENCE          1
             254 MAKE_FUNCTION            8
+            256 BUILD_LIST               1
+            258 DUP_TOP
+            260 LOAD_GLOBAL              1 (py_instrument_receiver)
+            262 ROT_TWO
+            264 LOAD_CONST               1 (125)
+            266 LOAD_CONST              25 ('f3')
+            268 LOAD_CONST              26 (12)
+            270 LOAD_CONST               4 (2)
+            272 LOAD_CONST               5 (False)
+            274 CALL_FUNCTION            6
+            276 POP_TOP
+            278 UNPACK_SEQUENCE          1
             280 STORE_FAST               2 (f3)
  17         282 LOAD_FAST                2 (f3)
+            284 BUILD_LIST               1
+            286 DUP_TOP
+            288 LOAD_GLOBAL              1 (py_instrument_receiver)
+            290 ROT_TWO
+            292 LOAD_CONST              27 (124)
+            294 LOAD_CONST              25 ('f3')
+            296 LOAD_CONST              28 (13)
+            298 LOAD_CONST               4 (2)
+            300 LOAD_CONST               9 (True)
+            302 CALL_FUNCTION            6
+            304 POP_TOP
+            306 UNPACK_SEQUENCE          1
+            308 BUILD_LIST               1
+            310 DUP_TOP
+            312 LOAD_GLOBAL              1 (py_instrument_receiver)
+            314 ROT_TWO
+            316 LOAD_CONST              29 (131)
+            318 LOAD_CONST              30 (0)
+            320 LOAD_CONST              31 (14)
+            322 LOAD_CONST               4 (2)
+            324 LOAD_CONST               5 (False)
+            326 CALL_FUNCTION            6
+            328 POP_TOP
+            330 UNPACK_SEQUENCE          1
             332 CALL_FUNCTION            0
+            334 BUILD_LIST               1
+            336 DUP_TOP
+            338 LOAD_GLOBAL              1 (py_instrument_receiver)
+            340 ROT_TWO
+            342 LOAD_CONST              29 (131)
+            344 LOAD_CONST              30 (0)
+            346 LOAD_CONST              31 (14)
+            348 LOAD_CONST               4 (2)
+            350 LOAD_CONST               9 (True)
+            352 CALL_FUNCTION            6
+            354 POP_TOP
+            356 UNPACK_SEQUENCE          1
             358 POP_TOP
+            360 LOAD_GLOBAL              1 (py_instrument_receiver)
+            362 BUILD_LIST               0
+            364 LOAD_CONST               3 (1)
+            366 LOAD_CONST               0 (None)
+            368 LOAD_CONST              32 (15)
+            370 LOAD_CONST               4 (2)
+            372 LOAD_CONST               9 (True)
+            374 CALL_FUNCTION            6
+            376 POP_TOP
             378 LOAD_CONST               0 (None)
+            380 BUILD_LIST               1
+            382 DUP_TOP
+            384 LOAD_GLOBAL              1 (py_instrument_receiver)
+            386 ROT_TWO
+            388 LOAD_CONST              13 (100)
+            390 LOAD_CONST               0 (None)
+            392 LOAD_CONST              33 (16)
+            394 LOAD_CONST               4 (2)
+            396 LOAD_CONST               9 (True)
+            398 CALL_FUNCTION            6
+            400 POP_TOP
+            402 UNPACK_SEQUENCE          1
             404 RETURN_VALUE

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
+            142 BUILD_LIST               1
+            144 DUP_TOP
+            146 LOAD_GLOBAL              1 (py_instrument_receiver)
+            148 ROT_TWO
+            150 LOAD_CONST              16 (100)
+            152 LOAD_CONST               0 (None)
+            154 LOAD_CONST              17 (6)
+            156 LOAD_CONST               4 (3)
+            158 LOAD_CONST              10 (True)
+            160 CALL_FUNCTION            6
+            162 POP_TOP
+            164 UNPACK_SEQUENCE          1
             166 RETURN_VALUE
'''

snapshots['test_scope_forwarding_loads (2, 3, 7)'] = [
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
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            2
        ]
    },
    {
        'arg': 'y',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 102,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 104,
        'stack': [
            3
        ]
    },
    {
        'arg': 'z',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 154,
        'stack': [
            3
        ]
    },
    {
        'arg': GenericRepr('<code object f1 at 0x100000000, file "<string>", line 5>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 156,
        'stack': [
            GenericRepr('<code object f1 at 0x100000000, file "<string>", line 5>')
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 182,
        'stack': [
            'f1'
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 234,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 236,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 286,
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
        'arg': 4,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 28,
        'stack': [
            4
        ]
    },
    {
        'arg': {
            'cell': 'w'
        },
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 82,
        'stack': [
            4
        ]
    },
    {
        'arg': 5,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 84,
        'stack': [
            5
        ]
    },
    {
        'arg': 'u',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 134,
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
        'orig_op': 136,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object f2 at 0x100000000, file "<string>", line 9>'),
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 168,
        'stack': [
            GenericRepr('<code object f2 at 0x100000000, file "<string>", line 9>')
        ]
    },
    {
        'arg': 'f1.<locals>.f2',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 194,
        'stack': [
            'f1.<locals>.f2'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 246,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 248,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 298,
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
        'arg': 6,
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 84,
        'stack': [
            6
        ]
    },
    {
        'arg': {
            'cell': 'u'
        },
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 138,
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
        'orig_op': 140,
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
        'orig_op': 170,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object f3 at 0x100000000, file "<string>", line 13>'),
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 202,
        'stack': [
            GenericRepr('<code object f3 at 0x100000000, file "<string>", line 13>')
        ]
    },
    {
        'arg': 'f1.<locals>.f2.<locals>.f3',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 228,
        'stack': [
            'f1.<locals>.f2.<locals>.f3'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 280,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 282,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 332,
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
        'arg': None,
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 140,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 332,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f2',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 358,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 378,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 298,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f1',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 324,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 344,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 286,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'POP_TOP',
        'orig_op': 312,
        'stack': [
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 332,
        'stack': [
            None
        ]
    }
]
