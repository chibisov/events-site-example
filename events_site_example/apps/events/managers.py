# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from django.db import models

#from apps.events.conditions import ProfileConditions


class EventTypeQuerySet(QuerySet):
    def filter_by_published(self):
        # todo: test me
        return self.all()
#        return self.filter(ProfileConditions.is_studying())


class EventTypeManager(models.Manager):
    def get_query_set(self):
        return EventTypeQuerySet(self.model, using=self._db)

    def filter_by_published(self):
        return self.get_query_set().filter_by_published()