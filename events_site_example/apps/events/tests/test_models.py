# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.events.factories import EventTypeFactory, EventFactory, LectureFactory


class TestEventTypeModel(TestCase):
    def setUp(self):
        self.event_type = EventTypeFactory.build(name=u'Yet another Conference')

    def test_get_absolute_url(self):
        self.event_type.slug = 'yac'
        expected = '/events/yac/'
        self.assertEqual(self.event_type.get_absolute_url(), expected)



class TestEventModel(TestCase):
    def setUp(self):
        self.event = EventFactory.build(name=u'Yac 2012')

    def test_get_absolute_url(self):
        self.event.type.slug = 'yac'
        self.event.slug = '2012'
        expected = '/events/yac/2012/'
        self.assertEqual(self.event.get_absolute_url(), expected)


class TestLectureModel(TestCase):
    def setUp(self):
        self.lecture = LectureFactory.build(name=u'Yandex and W3C', event__name=u'Yac 2012')

    def test_unicode(self):
        expected = u'Yandex and W3C on Yac 2012'
        self.assertEqual(self.lecture.__unicode__(), expected)

    def test_get_absolute_url(self):
        self.lecture.slug = 'yandex-w3c'
        expected = '/lectures/yandex-w3c/'
        self.assertEqual(self.lecture.get_absolute_url(), expected)