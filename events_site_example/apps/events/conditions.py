# -*- coding: utf-8 -*-
import datetime

from django.utils.timezone import now
from django.db.models import Q

from apps.common_app.utils import add_model_prefix as add


class EventTypeConditions(object):
    @classmethod
    def is_published(cls, model_instance=None, prefix=None):
        if model_instance:
            condition = model_instance.is_moderated
        else:
            condition = Q(**{add(prefix, 'is_moderated'): True})

        return condition


class EventConditions(object):
    @classmethod
    def is_published(cls, model_instance=None, prefix=None):
        kwargs = {
            'model_instance': model_instance,
            'prefix': prefix
        }

        return cls.is_it_time_to_publish(**kwargs) & cls.is_with_published_type(**kwargs)

    @classmethod
    def is_it_time_to_publish(cls, model_instance=None, prefix=None):
        two_days_later = now() + datetime.timedelta(days=2)

        if model_instance:
            condition = model_instance.date_start <= two_days_later
        else:
            condition = Q(**{add(prefix, 'date_start__lte'): two_days_later})

        return condition

    @classmethod
    def is_with_published_type(cls, model_instance=None, prefix=None):
        if model_instance:
            condition = model_instance.type.is_published
        else:
            condition = EventTypeConditions.is_published(prefix=add(prefix, 'type'))

        return condition


class LectureConditions(object):
    @classmethod
    def is_with_video(cls, model_instance=None, prefix=None):
        if model_instance:
            condition = bool(model_instance.video_url)
        else:
            condition = (Q(**{add(prefix, 'video_url__isnull'): False}) &
                        ~Q(**{add(prefix, 'video_url'): ''}))

        return condition

    @classmethod
    def is_with_published_event(cls, model_instance=None, prefix=None):
        if model_instance:
            event_instance = model_instance.event
        else:
            event_instance = None

        kwargs = {
            'model_instance': event_instance,
            'prefix': add(prefix, 'event')
        }
        return EventConditions.is_published(**kwargs)