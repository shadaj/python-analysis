# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_calls_to_module_function 1'] = [
    {
        'arg': GenericRepr('<code object other_func at 0x100000000, file "/home/shadaj/work/python-analysis/test/simple_module_to_import.py", line 1>'),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '<code object other_func at SOME ADDRESS, file "/home/shadaj/work/python-analysis/test/simple_module_to_import.py", line 1>'
        ]
    },
    {
        'arg': 'other_func',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'other_func'
        ]
    },
    {
        'arg': 'other_func',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'stack': [
            '<function other_func at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object hello at 0x100000000, file "/home/shadaj/work/python-analysis/test/simple_module_to_import.py", line 5>'),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '<code object hello at SOME ADDRESS, file "/home/shadaj/work/python-analysis/test/simple_module_to_import.py", line 5>'
        ]
    },
    {
        'arg': 'hello',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'hello'
        ]
    },
    {
        'arg': 'hello',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'stack': [
            '<function hello at SOME ADDRESS>'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '1'
        ]
    },
    {
        'arg': 'x',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '1'
        ]
    },
    {
        'arg': 0,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function other_func at SOME ADDRESS>'
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 'out',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 0,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 'y',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 'x',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '1'
        ]
    },
    {
        'arg': 'y',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': None,
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'stack': [
            '1',
            '2'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'stack': [
            '3'
        ]
    },
    {
        'arg': 'z',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '3'
        ]
    },
    {
        'arg': 'z',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '3'
        ]
    }
]

snapshots['test_calls_to_numpy_function (1, 3, 7)'] = [
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _makearray at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function asarray at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'dtype',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': False,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 'order',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': (
            'copy',
            'order'
        ),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            "('copy', 'order')"
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'new',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': '__array_prepare__',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '__array_prepare__'
        ]
    },
    {
        'arg': 'new',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': '__array_wrap__',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': '__array_wrap__',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<built-in method __array_wrap__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 3,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in function getattr>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]''',
            '__array_prepare__',
            '<built-in method __array_wrap__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 3,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in method __array_prepare__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'wrap',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '<built-in method __array_prepare__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'new',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'wrap',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '<built-in method __array_prepare__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '''(array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]), <built-in method __array_prepare__ of numpy.ndarray object at SOME ADDRESS>)'''
        ]
    },
    {
        'arg': 'a',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'wrap',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '<built-in method __array_prepare__ of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _assert_stacked_2d at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': {
            'label': 22
        },
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'stack': [
        ]
    },
    {
        'arg': 'arrays',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''(array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]),)'''
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arg': 'a',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'ndim',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'ndim',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '2'
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.LT'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            '2',
            '2'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.LT'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 4
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arrive_at': 20
    },
    {
        'arrive_at': 22
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'None'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'POP_TOP',
        'stack': [
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _assert_stacked_square at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': {
            'label': 27
        },
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'stack': [
        ]
    },
    {
        'arg': 'arrays',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''(array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]),)'''
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arg': 'a',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'shape',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'shape',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '(3, 3)'
        ]
    },
    {
        'arg': -2,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '-2'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': None,
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'stack': [
            '(3, 3)',
            'slice(-2, None, None)'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'stack': [
            '(3, 3)'
        ]
    },
    {
        'arg': 'm',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '3'
        ]
    },
    {
        'arg': 'n',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '3'
        ]
    },
    {
        'arg': 'm',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '3'
        ]
    },
    {
        'arg': 'n',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '3'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.NE'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            '3',
            '3'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.NE'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 4
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arrive_at': 25
    },
    {
        'arrive_at': 27
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'None'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'POP_TOP',
        'stack': [
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _assert_finite at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': {
            'label': 20
        },
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'stack': [
        ]
    },
    {
        'arg': 'arrays',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''(array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]),)'''
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arg': 'a',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "<ufunc 'isfinite'>",
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '''[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]'''
        ]
    },
    {
        'arg': 'axis',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'dtype',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'keepdims',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 5,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in method reduce of numpy.ufunc object at SOME ADDRESS>',
            '''[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]''',
            'None',
            'None',
            'None',
            'False'
        ]
    },
    {
        'arg': 5,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'True'
        ]
    },
    {
        'arg': {
            'label': 4
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_TRUE',
        'stack': [
            'True'
        ]
    },
    {
        'arrive_at': 4
    },
    {
        'arrive_at': 18
    },
    {
        'arrive_at': 20
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'None'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'POP_TOP',
        'stack': [
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _commonType at SOME ADDRESS>',
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'result_type',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float32'>"
        ]
    },
    {
        'arg': False,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 'is_complex',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 62
        },
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'stack': [
        ]
    },
    {
        'arg': 'arrays',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''(array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]),)'''
        ]
    },
    {
        'arrive_at': 8
    },
    {
        'arg': 'a',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'dtype',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'dtype',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            'int64'
        ]
    },
    {
        'arg': 'type',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            'int64'
        ]
    },
    {
        'arg': 'type',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            "<class 'numpy.int64'>"
        ]
    },
    {
        'arg': 2,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in function issubclass>',
            "<class 'numpy.int64'>",
            "<class 'numpy.inexact'>"
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 49
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 49
    },
    {
        'arg': 'rt',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arrive_at': 52
    },
    {
        'arg': 'rt',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            "<class 'numpy.float64'>",
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            'True'
        ]
    },
    {
        'arg': {
            'label': 8
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'True'
        ]
    },
    {
        'arg': 'result_type',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arrive_at': 8
    },
    {
        'arrive_at': 60
    },
    {
        'arrive_at': 62
    },
    {
        'arg': 'is_complex',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 72
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 72
    },
    {
        'arg': 't',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arrive_at': 75
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 'result_type',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "(<class 'numpy.float64'>, <class 'numpy.float64'>)"
        ]
    },
    {
        'arg': 't',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 'result_t',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function get_linalg_error_extobj at SOME ADDRESS>',
            '<function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "<class 'list'>",
            '[8192, 1536, None]'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '[8192, 1536, None]'
        ]
    },
    {
        'arg': 'extobj',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '[8192, 1536, None]'
        ]
    },
    {
        'arg': 'callback',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '<function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'extobj',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[8192, 1536, None]'
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '2'
        ]
    },
    {
        'arg': None,
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'stack': [
            '<function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>',
            '[8192, 1536, None]',
            '2'
        ]
    },
    {
        'arg': 'extobj',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[8192, 1536, <function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>]'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '[8192, 1536, <function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>]'
        ]
    },
    {
        'arg': 'extobj',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '[8192, 1536, <function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>]'
        ]
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function isComplexType at SOME ADDRESS>',
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 2,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in function issubclass>',
            "<class 'numpy.float64'>",
            "<class 'numpy.complexfloating'>"
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 35
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 35
    },
    {
        'arg': 'd->D',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'd->D'
        ]
    },
    {
        'arrive_at': 37
    },
    {
        'arg': 'signature',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            'd->D'
        ]
    },
    {
        'arg': 'eigvals',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<module numpy.linalg._umath_linalg>'
        ]
    },
    {
        'arg': 'eigvals',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            "<ufunc 'eigvals'>"
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '''[[1 0 0]
 [0 1 0]
 [0 0 1]]'''
        ]
    },
    {
        'arg': 'signature',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'd->D'
        ]
    },
    {
        'arg': 'extobj',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[8192, 1536, <function _raise_linalgerror_eigenvalues_nonconvergence at SOME ADDRESS>]'
        ]
    },
    {
        'arg': (
            'signature',
            'extobj'
        ),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            "('signature', 'extobj')"
        ]
    },
    {
        'arg': 'w',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '[1.+0.j 1.+0.j 1.+0.j]'
        ]
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function isComplexType at SOME ADDRESS>',
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 2,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<built-in function issubclass>',
            "<class 'numpy.float64'>",
            "<class 'numpy.complexfloating'>"
        ]
    },
    {
        'arg': 2,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 71
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_TRUE',
        'stack': [
            'False'
        ]
    },
    {
        'arg': 'w',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[1.+0.j 1.+0.j 1.+0.j]'
        ]
    },
    {
        'arg': 'imag',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '[1.+0.j 1.+0.j 1.+0.j]'
        ]
    },
    {
        'arg': 'imag',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '[0. 0. 0.]'
        ]
    },
    {
        'arg': 0,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '0'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            '[0. 0. 0.]',
            '0'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            '[ True  True  True]'
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function all at SOME ADDRESS>',
            '[ True  True  True]'
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[ True  True  True]'
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'a',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[ True  True  True]'
        ]
    },
    {
        'arg': 'logical_and',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<module numpy>'
        ]
    },
    {
        'arg': 'logical_and',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            "<ufunc 'logical_and'>"
        ]
    },
    {
        'arg': 'all',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'all'
        ]
    },
    {
        'arg': 'axis',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': None,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'keepdims',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '<no value>'
        ]
    },
    {
        'arg': (
            'keepdims'
        ,),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            "('keepdims',)"
        ]
    },
    {
        'arg': GenericRepr('<code object <dictcomp> at 0x100000000, file "/home/shadaj/work/python-analysis/.venv/lib/python3.7/site-packages/numpy/core/fromnumeric.py", line 71>'),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '<code object <dictcomp> at SOME ADDRESS, file "/home/shadaj/work/python-analysis/.venv/lib/python3.7/site-packages/numpy/core/fromnumeric.py", line 71>'
        ]
    },
    {
        'arg': '_wrapreduction.<locals>.<dictcomp>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            '_wrapreduction.<locals>.<dictcomp>'
        ]
    },
    {
        'arg': 'kwargs',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "{'keepdims': <no value>}"
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _wrapreduction.<locals>.<dictcomp> at SOME ADDRESS>',
            '<dict_itemiterator object at SOME ADDRESS>'
        ]
    },
    {
        'arg': '.0',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '<dict_itemiterator object at SOME ADDRESS>'
        ]
    },
    {
        'arrive_at': 3
    },
    {
        'arg': 'k',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            'keepdims'
        ]
    },
    {
        'arg': 'v',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '<no value>'
        ]
    },
    {
        'arg': 'v',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '<no value>'
        ]
    },
    {
        'arg': '_NoValue',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<module numpy>'
        ]
    },
    {
        'arg': '_NoValue',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<no value>'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS_NOT'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            '<no value>',
            '<no value>'
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS_NOT'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 3
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 3
    },
    {
        'arrive_at': 17
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '{}'
        ]
    },
    {
        'arg': 'passkwargs',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '{}'
        ]
    },
    {
        'arg': 'obj',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[ True  True  True]'
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "<class 'type'>",
            '[ True  True  True]'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "<class 'numpy.ndarray'>"
        ]
    },
    {
        'arg': 'ndarray',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<module numpy.core.multiarray>'
        ]
    },
    {
        'arg': 'ndarray',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            "<class 'numpy.ndarray'>"
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS_NOT'
        },
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'stack': [
            "<class 'numpy.ndarray'>",
            "<class 'numpy.ndarray'>"
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.IS_NOT'
        },
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'stack': [
            'False'
        ]
    },
    {
        'arg': {
            'label': 64
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'False'
        ]
    },
    {
        'arrive_at': 64
    },
    {
        'arg': 'ufunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<ufunc 'logical_and'>"
        ]
    },
    {
        'arg': 'reduce',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            "<ufunc 'logical_and'>"
        ]
    },
    {
        'arg': 'reduce',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<built-in method reduce of numpy.ufunc object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'obj',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[ True  True  True]'
        ]
    },
    {
        'arg': 'axis',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'dtype',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            'None'
        ]
    },
    {
        'arg': 'passkwargs',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '{}'
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            'True'
        ]
    },
    {
        'arg': {
            'label': 66
        },
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'stack': [
            'True'
        ]
    },
    {
        'arg': 'w',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[1.+0.j 1.+0.j 1.+0.j]'
        ]
    },
    {
        'arg': 'real',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '[1.+0.j 1.+0.j 1.+0.j]'
        ]
    },
    {
        'arg': 'real',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '[1. 1. 1.]'
        ]
    },
    {
        'arg': 'w',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            '[1. 1. 1.]'
        ]
    },
    {
        'arg': 'result_t',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            '<function _realType at SOME ADDRESS>',
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 't',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 'default',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 1,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': 'result_t',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arrive_at': 71
    },
    {
        'arg': 'w',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            '[1. 1. 1.]'
        ]
    },
    {
        'arg': 'astype',
        'is_post': False,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '[1. 1. 1.]'
        ]
    },
    {
        'arg': 'astype',
        'is_post': True,
        'opcode': 'LOAD_ATTR',
        'stack': [
            '<built-in method astype of numpy.ndarray object at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'result_t',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            "<class 'numpy.float64'>"
        ]
    },
    {
        'arg': False,
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            'False'
        ]
    },
    {
        'arg': (
            'copy'
        ,),
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'stack': [
            "('copy',)"
        ]
    }
]
