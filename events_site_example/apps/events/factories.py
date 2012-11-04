# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now

import factory

from apps.events.models import EventType, Event, Lecture


class EventTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = EventType

    name = factory.Sequence(lambda n: u'Event type {n}'.format(n=n))
    slug = factory.Sequence(lambda n: u'event-type-{n}'.format(n=n))


class EventFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Event

    name = factory.Sequence(lambda n: u'Event {n}'.format(n=n))
    slug = factory.Sequence(lambda n: u'event-{n}'.format(n=n))
    type = factory.SubFactory(EventTypeFactory)
    date_start = factory.LazyAttribute(lambda i: now() + datetime.timedelta(days=1))


class LectureFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Lecture

    name = factory.Sequence(lambda n: u'Lecture {n}'.format(n=n))
    slug = factory.Sequence(lambda n: u'lecture-{n}'.format(n=n))
    event = factory.SubFactory(EventFactory)
