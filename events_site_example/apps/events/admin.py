# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.events.models import EventType, Event, Lecture


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_published')

    def is_published(self, instance):
        return instance.is_published
    is_published.boolean = True


class EventAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'date_start', 'is_published')

    def is_published(self, instance):
        return instance.is_published
    is_published.boolean = True


class LectureAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'event', 'is_with_video', 'is_published')

    def is_published(self, instance):
        return instance.is_published
    is_published.boolean = True

    def is_with_video(self, instance):
        return instance.is_with_video
    is_with_video.boolean = True


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Lecture, LectureAdmin)