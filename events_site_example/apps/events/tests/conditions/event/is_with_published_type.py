# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import Event
from apps.events.factories import EventFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestEventIsWithPublishedType(TestConditionBase):
    model = Event
    queryset_method_name = 'filter_by_with_published_type'
    instance_property_name = 'is_with_published_type'

    def create_instance(self):
        return EventFactory()

    def test_should_be_true_if__type_is_published__is_true(self):
        msg = 'should be True, if event.type is published'
        makers.event_type.make_published(self.instance.type)

        self.assertConditionTrue(msg=msg)

    def test_should_be_false_if__type_is_published__is_false(self):
        msg = 'should be False, if event.type is not published'
        makers.event_type.make_not_published(self.instance.type)

        self.assertConditionFalse(msg=msg)

    def test_make_with_published_type(self):
        msg = "make_with_published_type should make event with published type"

        # make type not published by hand
        makers.event_type.make_not_published(self.instance.type)
        self.instance.type.save()

        makers.event.make_with_published_type(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_with_published_type(self):
        msg = "make_with_not_published_type should make event with not published type"

        # make type published by hand
        makers.event_type.make_published(self.instance.type)
        self.instance.type.save()

        makers.event.make_not_with_published_type(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)