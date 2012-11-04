# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now

from apps.events import makers
from apps.events.models import Event
from apps.events.factories import EventFactory
from apps.common_app.tests.helpers import TestConditionBase


class TestEventIsItTimeToPublish(TestConditionBase):
    model = Event
    queryset_method_name = 'filter_by_it_time_to_publish'
    instance_property_name = 'is_it_time_to_publish'

    def create_instance(self):
        return EventFactory()

    def save_instance(self, instance):
        instance.save()

    def test_should_be_true_if__date_start__lte__2_days_from_now_in_future(self):
        msg = 'should be True, if event.date_start is 2 days or less from now in future. '

        for i in range(2):
            self.instance.date_start = now() + datetime.timedelta(days=i)
            msg += 'Tested with {days} days'.format(days=i)

            self.assertConditionTrue(msg=msg)

    def test_should_be_false_if__date_start__gt__2_days_from_now(self):
        msg = 'should be False, if event.date_start is more than 2 days in future'
        self.instance.date_start = now() + datetime.timedelta(days=3)

        self.assertConditionFalse(msg=msg)

    def test_make_it_time_to_publish(self):
        msg = "make_it_time_to_publish should make event is ready to publish by time"

        # make type not time to published by hand
        self.instance.date_start = now() + datetime.timedelta(days=3)
        self.instance.save()

        makers.event.make_it_time_to_publish(self.instance) # BANG!

        self.assertConditionTrue(msg=msg)

    def test_make_not_it_time_to_publish(self):
        msg = "make_not_it_time_to_publish should make event is not ready to publish by time"

        # make type not time to published by hand
        self.instance.date_start = now()
        self.instance.save()

        makers.event.make_not_it_time_to_publish(self.instance) # BANG!

        self.assertConditionFalse(msg=msg)