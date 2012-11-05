# -*- coding: utf-8 -*-
from apps.events import makers
from apps.events.models import EventType
from apps.events.factories import EventTypeFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestEventTypeIsPublished(TestConditionBase):
    model = EventType
    queryset_method_name = 'filter_by_published'
    instance_property_name = 'is_published'

    def create_instance(self):
        return EventTypeFactory()

    def test_should_be_published_if__is_moderated__is_true(self):
        msg = 'event type should be published if "is_moderated" is True'
        self.instance.is_moderated = True
        self.instance.save()

        self.assertConditionTrue(msg=msg)

    def test_should_not_be_published_if__is_moderated__is_false(self):
        msg = 'event type should not be published if "is_moderated" is False'
        self.instance.is_moderated = False
        self.instance.save()

        self.assertConditionFalse(msg=msg)

    def test_make_published(self):
        msg = 'make_published should make event type published'

        # make not published by hand
        self.instance.is_moderated = False
        self.instance.save()

        makers.event_type.make_published(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_published(self):
        msg = 'make_not_published should make event type not published'

        # make published by hand
        self.instance.is_moderated = True
        self.instance.save()

        makers.event_type.make_not_published(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)
