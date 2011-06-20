"""Urls for the Zinnia discussions"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns
import zinnia.views

urlpatterns = patterns('',
                       url(r'^success/$', 'views.comment_posted',
                           {'template': 'comments/zinnia/entry/posted.html'},
                           name='zinnia_discussion_success'),
                       )
