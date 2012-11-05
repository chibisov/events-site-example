# -*- coding: utf-8 -*-
from apps.events.makers import event


def make_with_video(lecture):
    lecture.video_url = 'http://www.youtube.com/watch?v=oHg5SJYRHA0'

def make_not_with_video(lecture):
    lecture.video_url = None

def make_with_published_event(lecture):
    event.make_published(lecture.event)

def make_not_with_published_event(lecture):
    event.make_not_published(lecture.event)