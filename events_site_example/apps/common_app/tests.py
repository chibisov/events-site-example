# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.common_app.utils import add_model_prefix


class TestUtils(TestCase):
    def test_add_model_prefix(self):
        experiments = [
            {
                'prefix': None,
                'to': 'some_value',
                'expected': 'some_value',
                'msg': 'if "prefix" is not set, then "to" should be returned'
            },
            {
                'prefix': 'prefix',
                'to': 'some_value',
                'expected': 'prefix__some_value',
                'msg': 'if "prefix" is set, then "prefix" should be concatenated to "to" with two underscores'
            }
        ]

        for exp in experiments:
            response = add_model_prefix(exp['prefix'], exp['to'])
            self.assertEqual(response, exp['expected'], msg=exp['msg'])
