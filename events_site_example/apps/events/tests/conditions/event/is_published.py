# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import Event
from apps.events.factories import EventFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestEventIsPublished(TestConditionBase):
    model = Event
    queryset_method_name = 'filter_by_published'
    instance_property_name = 'is_published'

    def create_instance(self):
        return EventFactory()

    def test_should_be_true_if__type_is_published__and__event_is_ready_to_publish_by_time(self):
        msg = 'should be True, if event.type is published and event is ready to publish by time'
        makers.event_type.make_published(self.instance.type)
        makers.event.make_it_time_to_publish(self.instance)

        self.assertConditionTrue(msg=msg)

    def test_should_be_true_if__type_is_published__but__event_is_not_ready_to_publish_by_time(self):
        msg = 'should be False, if event.type is published, but event is not ready to publish by time'
        makers.event_type.make_published(self.instance.type)
        makers.event.make_not_it_time_to_publish(self.instance)

        self.assertConditionFalse(msg=msg)

    def test_should_be_true_if__event_is_ready_to_publish_by_time__but__type_is_not_published(self):
        msg = 'should be False, if event is ready to publish by time, but is not event.type is not published'
        makers.event.make_it_time_to_publish(self.instance)
        makers.event_type.make_not_published(self.instance.type)

        self.assertConditionFalse(msg=msg)

    def test_make_published(self):
        msg = "make_published should make event is published"

        # make event not published by hand
        makers.event_type.make_not_published(self.instance.type)
        makers.event.make_not_it_time_to_publish(self.instance)

        makers.event.make_published(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_not_make_published(self):
        msg = "make_not_published should make event is not published"

        # make event not published by hand
        makers.event_type.make_published(self.instance.type)
        makers.event.make_it_time_to_publish(self.instance)

        makers.event.make_not_published(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)