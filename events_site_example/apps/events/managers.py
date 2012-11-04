# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from django.db import models

from apps.events.conditions import EventTypeConditions, EventConditions


class EventTypeQuerySet(QuerySet):
    def filter_by_published(self):
        return self.filter(EventTypeConditions.is_published())


class EventTypeManager(models.Manager):
    def get_query_set(self):
        return EventTypeQuerySet(self.model, using=self._db)

    def filter_by_published(self):
        return self.get_query_set().filter_by_published()


class EventQuerySet(QuerySet):
    def filter_by_with_published_type(self):
        return self.filter(EventConditions.is_with_published_type())

    def filter_by_it_time_to_publish(self):
        return self.filter(EventConditions.is_it_time_to_publish())

    def filter_by_published(self):
        return self.filter(EventConditions.is_published())


class EventManager(models.Manager):
    def get_query_set(self):
        return EventQuerySet(self.model, using=self._db)

    def filter_by_with_published_type(self):
        return self.get_query_set().filter_by_with_published_type()

    def filter_by_it_time_to_publish(self):
        return self.get_query_set().filter_by_it_time_to_publish()

    def filter_by_published(self):
        return self.get_query_set().filter_by_published()