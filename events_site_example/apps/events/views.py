# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, RedirectView

from apps.events.models import EventType, Event, Lecture


class IndexPage(RedirectView):
    url = '/events/'


class EventTypeListView(ListView):
    queryset = EventType.objects.all()


class EventTypeDetailView(DetailView):
    queryset = EventType.objects.all()
    slug_url_kwarg = 'eventtype_slug'


class EventDetailView(DetailView):
    queryset = Event.objects.all()
    slug_url_kwarg = 'event_slug'

    def get_queryset(self):
        queryset = super(EventDetailView, self).get_queryset()
        return queryset.filter(type__slug=self.kwargs['eventtype_slug'])


class LectureListView(ListView):
    queryset = Lecture.objects.all()


class LectureDetailView(DetailView):
    queryset = Lecture.objects.all()