# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import Lecture
from apps.events.factories import LectureFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestLectureIsWithVideo(TestConditionBase):
    model = Lecture
    queryset_method_name = 'filter_by_with_video'
    instance_property_name = 'is_with_video'

    def create_instance(self):
        return LectureFactory()

    def save_instance(self, instance):
        instance.save()

    def test_should_be_true_if__video_url__is_filled(self):
        msg = 'if lecture has filled "video_url" param, then it should be with video'
        self.instance.video_url = 'http://www.youtube.com/watch?v=oHg5SJYRHA0'

        self.assertConditionTrue(msg=msg)

    def test_should_be_false_if__video_url__is_none(self):
        msg = 'if lecture has filled "video_url" param with None, then it should not be with video'
        self.instance.video_url = None

        self.assertConditionFalse(msg=msg)

    def test_should_be_false_if__video_url__is_empty(self):
        msg = 'if lecture has filled "video_url" param with "", then it should not be with video'
        self.instance.video_url = ''

        self.assertConditionFalse(msg=msg)

    def test_make_with_video(self):
        msg = "make_with_video should make lecture with video"

        # make lecture without video by hand
        self.instance.video_url = None

        makers.lecture.make_with_video(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_with_video(self):
        msg = "make_not_with_video should make lecture without video"

        # make lecture with video by hand
        self.instance.video_url = 'http://www.youtube.com/watch?v=oHg5SJYRHA0'

        makers.lecture.make_not_with_video(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)