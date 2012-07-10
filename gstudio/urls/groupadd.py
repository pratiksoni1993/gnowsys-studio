"""Url for Gstudio User Dashboard"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.groupadd',
                       url(r'^$', 'groupadd',
                           name='gstudio_grp'),

                       )
