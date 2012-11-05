# -*- coding: utf-8 -*-
from apps.accounts import makers
from apps.accounts.models import Profile
from apps.accounts.factories import ProfileFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestProfileIsStudying(TestConditionBase):
    model = Profile
    queryset_method_name = 'filter_by_studying'
    instance_property_name = 'is_studying'

    def create_instance(self):
        return ProfileFactory()

    def test_should_find_if__study_place__is_filled(self):
        msg = 'profile has filled "study_place" param. He should be studying'
        self.instance.study_place = u'MGUPI'
        self.instance.save()

        self.assertConditionTrue(msg=msg)

    def test_should_not_find_if__study_place__is_none(self):
        msg = 'profile has filled "study_place" param with None. He should not be studying'
        self.instance.study_place = None
        self.instance.save()

        self.assertConditionFalse(msg=msg)

    def test_should_not_find_if__study_place__is_empty(self):
        msg = 'profile has empty field "study_place". He should not be studying'
        self.instance.study_place = ''
        self.instance.save()

        self.assertConditionFalse(msg=msg)

    def test_make_studying(self):
        msg = 'make_studying should make profile studying'

        # make not studying by hand
        self.instance.study_place = None
        self.instance.save()

        makers.profile.make_studying(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_studying(self):
        msg = 'make_not_studying should make profile not studying'

        # make studying by hand
        self.instance.study_place = u'MGUPI'
        self.instance.save()

        makers.profile.make_not_studying(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)