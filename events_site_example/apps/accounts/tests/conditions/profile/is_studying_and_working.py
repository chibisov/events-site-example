# -*- coding: utf-8 -*-
from apps.accounts import makers
from apps.accounts.models import Profile
from apps.accounts.factories import ProfileFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestProfileIsStudyingAndWorking(TestConditionBase):
    model = Profile
    queryset_method_name = 'filter_by_studying_and_working'
    instance_property_name = 'is_studying_and_working'

    def create_instance(self):
        return ProfileFactory()

    def test_should_find_if_profile_is__studying_and_workging(self):
        msg = 'if profile is studying and working, then it should be "studying_and_working"'
        makers.profile.make_studying(self.instance)
        makers.profile.make_working(self.instance)

        self.assertConditionTrue(msg=msg)

    def test_should_not_find_if_profile__is_studying__but__not_working(self):
        msg = 'if profile is studying, but not is working, then it should not be "studying_and_working"'
        makers.profile.make_not_studying(self.instance)
        makers.profile.make_working(self.instance)

        self.assertConditionFalse(msg=msg)

    def test_should_not_find_if__is_working__but__not_studying(self):
        msg = 'if profile is working, but not is studying, then it should not be "studying_and_working"'
        makers.profile.make_studying(self.instance)
        makers.profile.make_not_working(self.instance)

        self.assertConditionFalse(msg=msg)

    def test_make_studying_and_working(self):
        msg = 'make_studying_and_working should make profile studying and working'

        # make not studying_and_working by hand
        makers.profile.make_not_studying(self.instance)
        makers.profile.make_not_working(self.instance)

        makers.profile.make_studying_and_working(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_studying_and_working(self):
        msg = 'make_not_studying_and_working should make profile not studying and working'

        # make studying_and_working by hand
        makers.profile.make_studying(self.instance)
        makers.profile.make_working(self.instance)

        makers.profile.make_not_studying_and_working(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)