# -*- coding: utf-8 -*-
from django.db import models

from apps.events.managers import EventTypeManager, EventManager
from apps.events.conditions import EventTypeConditions, EventConditions


class EventType(models.Model):
    """

    Example: Yet Another Conference

    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_moderated = models.BooleanField(default=False)

    objects = EventTypeManager()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'eventtype-path', (), {'eventtype_slug': self.slug}

    @property
    def is_published(self):
        return EventTypeConditions.is_published(model_instance=self)


class Event(models.Model):
    """

    Example: Yac 2012

    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    type = models.ForeignKey(EventType)
    date_start = models.DateTimeField()

    objects = EventManager()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'event-path', (), {'eventtype_slug': self.type.slug, 'event_slug': self.slug}

    @property
    def is_with_published_type(self):
        return EventConditions.is_with_published_type(model_instance=self)

    @property
    def is_it_time_to_publish(self):
        return EventConditions.is_it_time_to_publish(model_instance=self)

    @property
    def is_published(self):
        return EventConditions.is_published(model_instance=self)


class Lecture(models.Model):
    """

    Example: Yandex and W3C on Yac 2012

    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    event = models.ForeignKey(Event)
    video_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'{name} on {event_name}'.format(name=self.name, event_name=self.event.name)

    @models.permalink
    def get_absolute_url(self):
        return 'lecture-path', (), {'slug': self.slug}