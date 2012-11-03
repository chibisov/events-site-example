# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.accounts import makers
from apps.accounts.models import Profile
from apps.accounts.factories import ProfileFactory


class TestProfileIsStudying(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()

        # leave only 1 model instance
        Profile.objects.all().exclude(pk=self.profile.pk).delete()

    def assertInstanceMethodResponseReturns(self, response, msg):
        self.assertEqual(self.profile.is_studying, response, msg=msg)

    def assertFound(self, msg):
        self.assertEqual(Profile.objects.filter_by_studying().count(), 1, msg=msg)
        self.assertEqual(Profile.objects.filter_by_studying().all()[0], self.profile, msg=msg)

    def assertNotFound(self, msg):
        self.assertEqual(Profile.objects.filter_by_studying().count(), 0, msg=msg)

    def test_should_find_if__study_place__is_filled(self):
        msg = 'profile has filled "study_place" param. He should be studying'
        self.profile.study_place = u'MGUPI'

        # test instance method
        self.assertInstanceMethodResponseReturns(True, msg=msg)

        # test QuerySet filter method
        self.profile.save()
        self.assertFound(msg=msg)

    def test_should_not_find_if__study_place__is_none(self):
        msg = 'profile has filled "study_place" param with None. He should not be studying'
        self.profile.study_place = None

        # test instance method
        self.assertInstanceMethodResponseReturns(False, msg=msg)

        # test QuerySet filter method
        self.profile.save()
        self.assertNotFound(msg=msg)

    def test_should_not_find_if__param_study_place__is_empty(self):
        msg = 'profile has empty field "study_place". He should not be studying'
        self.profile.study_place = ''

        # test instance method
        self.assertInstanceMethodResponseReturns(False, msg=msg)

        # test QuerySet filter method
        self.profile.save()
        self.assertNotFound(msg=msg)

    def test_make_studying(self):
        msg = 'make_studying should make profile studying'

        # make not studying by hand
        self.profile.study_place = None
        self.profile.save()

        makers.profile.make_studying(self.profile) # BANG!

        # test instance method, which processed by maker
        self.assertInstanceMethodResponseReturns(True, msg=msg)

        # test that maker effect stays after saving
        self.profile.save()
        self.assertFound(msg=msg)

    def test_make_not_studying(self):
        msg = 'make_not_studying should make profile not studying'

        # make studying by hand
        self.profile.study_place = u'MGUPI'
        self.profile.save()

        makers.profile.make_not_studying(self.profile) # BANG!

        # test instance method, which processed by maker
        self.assertInstanceMethodResponseReturns(False, msg=msg)

        # test that maker effect stays after saving
        self.profile.save()
        self.assertNotFound(msg=msg)