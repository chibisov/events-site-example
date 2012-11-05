# -*- coding: utf-8 -*-


def make_studying(profile):
    profile.study_place = u'MGUPI'
    profile.save()

def make_not_studying(profile):
    profile.study_place = None
    profile.save()

def make_working(profile):
    profile.job_place = u'Yandex'
    profile.save()

def make_not_working(profile):
    profile.job_place = None
    profile.save()

def make_studying_and_working(profile):
    make_studying(profile)
    make_working(profile)

def make_not_studying_and_working(profile):
    make_not_studying(profile)