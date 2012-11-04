# -*- coding: utf-8 -*-
import datetime

from django.utils.timezone import now

from apps.events.makers import event_type


def make_with_published_type(event):
    event_type.make_published(event.type)

def make_not_with_published_type(event):
    event_type.make_not_published(event.type)

def make_it_time_to_publish(event):
    event.date_start = now() + datetime.timedelta(days=2)

def make_not_it_time_to_publish(event):
    event.date_start = now() + datetime.timedelta(days=3)

def make_published(event):
    event_type.make_published(event.type)
    make_it_time_to_publish(event)

def make_not_published(event):
    event_type.make_not_published(event.type)
    make_not_it_time_to_publish(event)