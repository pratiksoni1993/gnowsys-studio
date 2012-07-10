"""Url for Gstudio User Dashboard"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.group',
                       url(r'^gnowsys-grp/(\d+)/$', 'groupdashboard', name='gstudio_group'),
                     url(r'^later$', 'grouplater', name='gstudio_group'),
                      url(r'^over$', 'groupover',
                           name='gstudio_group'),
                       )
