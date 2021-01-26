# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_calls_to_module_function 1'] = [
    {
        'arg': 'other_func',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'stack': [
            '<function other_func at SOME ADDRESS>'
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
        'arg': 'x',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            1
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
        'arg': 'out',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            2
        ]
    },
    {
        'arg': 'out',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            2
        ]
    },
    {
        'arg': 0,
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'stack': [
            2
        ]
    },
    {
        'arg': 'y',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            2
        ]
    },
    {
        'arg': 'x',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            1
        ]
    },
    {
        'arg': 'y',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            2
        ]
    },
    {
        'arg': 'z',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'stack': [
            3
        ]
    },
    {
        'arg': 'z',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'stack': [
            3
        ]
    }
]
