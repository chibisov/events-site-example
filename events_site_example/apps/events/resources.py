# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource

from apps.events.models import EventType, Event, Lecture


class EventTypeResource(ModelResource):
    class Meta:
        queryset = EventType.objects.filter_by_published()


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.filter_by_published()


class LectureResource(ModelResource):
    class Meta:
        queryset = Lecture.objects.filter_by_published()
