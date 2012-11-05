# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import Lecture
from apps.events.factories import LectureFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestLectureIsPublished(TestConditionBase):
    model = Lecture
    queryset_method_name = 'filter_by_published'
    instance_property_name = 'is_published'

    def create_instance(self):
        return LectureFactory()

    def save_instance(self, instance):
        instance.save()
        instance.event.save()
        instance.event.type.save()

    def test_should_be_true__if_is_with_published_event__and__is_with_video(self):
        msg = 'lecture should be published, if it is with published event and with video'

        makers.lecture.make_with_published_event(self.instance)
        makers.lecture.make_with_video(self.instance)

        self.assertConditionTrue(msg=msg)

    def test_should_be_false__if_is_with_published_event__but__without_video(self):
        msg = 'lecture should not be published, if it is with published event, but without video'

        makers.lecture.make_with_published_event(self.instance)
        makers.lecture.make_not_with_video(self.instance)

        self.assertConditionFalse(msg=msg)

    def test_should_be_false__if_is_with_video__but__without_published_event(self):
        msg = 'lecture should not be published, if it is with video, but without published event'

        makers.lecture.make_with_video(self.instance)
        makers.lecture.make_not_with_published_event(self.instance)
        self.assertConditionFalse(msg=msg)

    def test_make_published(self):
        msg = "make_published should make lecture published"

        # make lecture not published by hand
        makers.lecture.make_not_with_published_event(self.instance)
        makers.lecture.make_not_with_video(self.instance)

        makers.lecture.make_published(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_published(self):
        msg = "make_not_published should make lecture not published"

        # make lecture not published by hand
        makers.lecture.make_with_published_event(self.instance)
        makers.lecture.make_with_video(self.instance)

        makers.lecture.make_not_published(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)