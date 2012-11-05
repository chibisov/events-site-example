# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import Lecture
from apps.events.factories import LectureFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestLectureIsWithPublishedEvent(TestConditionBase):
    model = Lecture
    queryset_method_name = 'filter_by_with_published_event'
    instance_property_name = 'is_with_published_event'

    def create_instance(self):
        return LectureFactory()

    def save_instance(self, instance):
        instance.save()
        instance.event.save()
        instance.event.type.save()

    def test_should_be_true__if_event_is_published(self):
        msg = 'lecture should be with published event if event is published'

        makers.event.make_published(self.instance.event)

        self.assertConditionTrue(msg=msg)

    def test_should_be_false_if_event_is_not_published(self):
        msg = 'lecture should be without published event if event is not published'

        makers.event.make_not_published(self.instance.event)

        self.assertConditionFalse(msg=msg)

    def test_make_with_published_event(self):
        msg = "make_with_published_event should make lecture with published event"

        # make lecture.event not published by hand
        makers.event.make_not_published(self.instance.event)

        makers.lecture.make_with_published_event(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_with_published_event(self):
        msg = "make_not_with_published_event should make lecture without published event"

        # make lecture.event published by hand
        makers.event.make_published(self.instance.event)

        makers.lecture.make_not_with_published_event(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)