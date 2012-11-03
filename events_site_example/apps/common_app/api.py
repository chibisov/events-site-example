# -*- coding: utf-8 -*-
from tastypie.api import Api

from apps.events.resources import EventTypeResource, EventResource, LectureResource


v1_api = Api(api_name='v1')
v1_api.register(EventTypeResource())
v1_api.register(EventResource())
v1_api.register(LectureResource())