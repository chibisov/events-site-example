# -*- coding: utf-8 -*-

def make_published(event_type):
    event_type.is_moderated = True

def make_not_published(event_type):
    event_type.is_moderated = False