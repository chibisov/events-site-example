# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource

from apps.events.models import EventType, Event, Lecture


class EventTypeResource(ModelResource):
    class Meta:
        queryset = EventType.objects.all()


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()


class LectureResource(ModelResource):
    class Meta:
        queryset = Lecture.objects.all()
