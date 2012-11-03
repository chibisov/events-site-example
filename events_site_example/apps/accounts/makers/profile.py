# -*- coding: utf-8 -*-


def make_studying(profile):
    profile.study_place = u'MGUPI'

def make_not_studying(profile):
    profile.study_place = None

def make_working(profile):
    # todo: test me
    profile.param_job_place = u'Yandex'

def make_not_working(profile):
    # todo: test me
    profile.param_job_place = None

def make_studying_and_working(profile):
    # todo: test me
    make_studying(profile)
    make_working(profile)

def make_not_studying_and_working(profile):
    # todo: test me
    make_not_studying(profile)