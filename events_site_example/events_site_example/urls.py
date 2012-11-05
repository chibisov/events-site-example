from django.conf.urls import patterns, include, url

from apps.common_app.api import v1_api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'', include('apps.events.urls')),
    # Examples:
    # url(r'^$', 'events_site_example.views.home', name='home'),
    # url(r'^events_site_example/', include('events_site_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
