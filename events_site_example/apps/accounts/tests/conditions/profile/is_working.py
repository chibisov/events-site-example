# -*- coding: utf-8 -*-
from apps.accounts import makers
from apps.accounts.models import Profile
from apps.accounts.factories import ProfileFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestProfileIsWorking(TestConditionBase):
    model = Profile
    queryset_method_name = 'filter_by_working'
    instance_property_name = 'is_working'

    def create_instance(self):
        return ProfileFactory()

    def test_should_find_if__job_place__is_filled(self):
        msg = 'profile has filled "job_place" param. He should be working'
        self.instance.job_place = u'Yandex'
        self.instance.save()

        self.assertConditionTrue(msg=msg)

    def test_should_not_find_if__job_place__is_none(self):
        msg = 'profile has filled "job_place" param with None. He should not be working'
        self.instance.job_place = None
        self.instance.save()

        self.assertConditionFalse(msg=msg)

    def test_should_not_find_if__job_place__is_empty(self):
        msg = 'profile has empty field "job_place". He should not be working'
        self.instance.job_place = ''
        self.instance.save()

        self.assertConditionFalse(msg=msg)

    def test_make_working(self):
        msg = 'make_working should make profile working'

        # make not working by hand
        self.instance.job_place = None
        self.instance.save()

        makers.profile.make_working(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_working(self):
        msg = 'make_not_working should make profile not working'

        # make working by hand
        self.instance.job_place = u'Yandex'
        self.instance.save()

        makers.profile.make_not_working(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)