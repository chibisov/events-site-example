# -*- coding: utf-8 -*-

def make_published(event_type):
    event_type.is_moderated = True
    event_type.save()

def make_not_published(event_type):
    event_type.is_moderated = False
    event_type.save()