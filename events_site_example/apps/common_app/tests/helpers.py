# -*- coding: utf-8 -*-
from django.test import TestCase


class TestConditionBase(TestCase):
#    model = ModelClass
#    queryset_method_name = 'queryset_filter_method_name'
#    instance_property_name = 'model_instance_property_name'

    def setUp(self):
        self.instance = self.create_instance()

        # leave only 1 model instance
        self.model.objects.all().exclude(pk=self.instance.pk).delete()
        self.queryset_filter_method = getattr(self.model.objects, self.queryset_method_name)

    def create_instance(self):
        """Creates instance of model"""
        raise NotImplementedError('Subclasses must define this method.')

    def save_instance(self):
        """Saves instance for queryset filtering"""
        raise NotImplementedError('Subclasses must define this method.')

    def assertInstanceMethodResponseReturns(self, response, msg):
        self.assertEqual(getattr(self.instance, self.instance_property_name), response, msg=msg)

    def assertFound(self, msg):
        self.assertEqual(self.queryset_filter_method().count(), 1, msg=msg)
        self.assertEqual(self.queryset_filter_method()[0], self.instance, msg=msg)

    def assertNotFound(self, msg):
        self.assertEqual(self.queryset_filter_method().count(), 0, msg=msg)

    def assertConditionTrue(self, msg=None):
        # test instance method
        self.assertInstanceMethodResponseReturns(True, msg=msg)

        # test QuerySet filter method
        self.save_instance(instance=self.instance)
        self.assertFound(msg=msg)

    def assertConditionFalse(self, msg=None):
        # test instance method
        self.assertInstanceMethodResponseReturns(False, msg=msg)

        # test QuerySet filter method
        self.save_instance(instance=self.instance)
        self.assertNotFound(msg=msg)