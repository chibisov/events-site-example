# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from apps.events.views import (IndexPage,
                               EventTypeListView,
                               EventTypeDetailView,
                               EventDetailView,
                               LectureListView,
                               LectureDetailView)


urlpatterns = patterns('',
    url(r'^$', IndexPage.as_view(), name='index-path'),
    url(r'^events/$', EventTypeListView.as_view(), name='events-path'),
    url(r'^events/(?P<eventtype_slug>[-\w]+)/$', EventTypeDetailView.as_view(), name='eventtype-path'),
    url(r'^events/(?P<eventtype_slug>[-\w]+)/(?P<event_slug>[-\w]+)/$', EventDetailView.as_view(), name='event-path'),
    url(r'^lectures/$', LectureListView.as_view(), name='lectures-path'),
    url(r'^lectures/(?P<slug>[-\w]+)/$', LectureDetailView.as_view(), name='lecture-path'),
)