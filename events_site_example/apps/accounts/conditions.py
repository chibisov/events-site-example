# -*- coding: utf-8 -*-
from django.db.models import Q

from apps.common_app.utils import add_model_prefix as add


class ProfileConditions(object):
    @classmethod
    def is_studying_and_working(cls, model_instance=None, prefix=None):
        """

        @type model_instance: apps.accounts.models.Profile

        """
        kwargs = {
            'model_instance': model_instance,
            'prefix': prefix
        }
        condition = cls.is_studying(**kwargs) & cls.is_working(**kwargs)

        return condition

    @classmethod
    def is_studying(cls, model_instance=None, prefix=None):
        """

        @type model_instance: apps.accounts.models.Profile

        """
        if model_instance:
            condition = bool(model_instance.study_place)
        else:
            condition = (Q(**{add(prefix, to='study_place__isnull'): False}) &
                        ~Q(**{add(prefix, to='study_place'): ''}))

        return condition

    @classmethod
    def is_working(cls, model_instance=None, prefix=None):
        """

        @type model_instance: apps.accounts.models.Profile

        """
        if model_instance:
            condition = bool(model_instance.job_place)
        else:
            condition = (Q(**{add(prefix, to='job_place__isnull'): False}) &
                         ~Q(**{add(prefix, to='job_place'): ''}))

        return condition