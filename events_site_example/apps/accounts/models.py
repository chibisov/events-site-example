# -*- coding: utf-8 -*-
from django.db import models

from apps.accounts.conditions import ProfileConditions
from apps.accounts.managers import ProfileManager


class Profile(models.Model):
    name = models.CharField(max_length=100)
    study_place = models.CharField(max_length=255, blank=True, null=True)
    job_place = models.CharField(max_length=255, blank=True, null=True)

    objects = ProfileManager()

    def __unicode__(self):
        return self.name

    @property
    def is_studying(self):
        # todo: test me
        return ProfileConditions.is_studying(model_instance=self)

    @property
    def is_working(self):
        # todo: test me
        return ProfileConditions.is_working(model_instance=self)

    @property
    def is_studying_and_working(self):
        # todo: test me
        return ProfileConditions.is_studying_and_working(model_instance=self)