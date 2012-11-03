# -*- coding: utf-8 -*-
from django.db import models


class EventType(models.Model):
    """

    Example: Yet Another Conference

    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'eventtype-path', (), {'eventtype_slug': self.slug}


class Event(models.Model):
    """

    Example: Yac 2012

    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    type = models.ForeignKey(EventType)
    date_start = models.DateTimeField()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'event-path', (), {'eventtype_slug': self.type.slug, 'event_slug': self.slug}


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