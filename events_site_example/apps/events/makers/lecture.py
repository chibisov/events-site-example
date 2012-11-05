# -*- coding: utf-8 -*-
from apps.events.makers import event


def make_with_video(lecture):
    lecture.video_url = 'http://www.youtube.com/watch?v=oHg5SJYRHA0'
    lecture.save()

def make_not_with_video(lecture):
    lecture.video_url = None
    lecture.save()

def make_with_published_event(lecture):
    event.make_published(lecture.event)

def make_not_with_published_event(lecture):
    event.make_not_published(lecture.event)

def make_published(lecture):
    event.make_published(lecture.event)
    make_with_video(lecture)

def make_not_published(lecture):
    event.make_not_published(lecture.event)
    make_not_with_video(lecture)