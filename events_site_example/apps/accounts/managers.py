# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from django.db import models

from apps.accounts.conditions import ProfileConditions


class ProfileQuerySet(QuerySet):
    def filter_by_studying(self):
        return self.filter(ProfileConditions.is_studying())

    def filter_by_working(self):
        # todo: test me
        return self.filter(ProfileConditions.is_working())

    def filter_by_studying_and_working(self):
        # todo: test me
        return self.filter(ProfileConditions.is_studying_and_working())


class ProfileManager(models.Manager):
    def get_query_set(self):
        return ProfileQuerySet(self.model, using=self._db)

    def filter_by_studying(self):
        return self.get_query_set().filter_by_studying()