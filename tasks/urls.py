"""Defines URL patterns for tasks."""


from django.conf.urls import url
from . import views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_note/(?P<topic_id>\d+)/$', views.new_note, name='new_note'),
    url(r'^edit_note/(?P<note_id>\d+)/$', views.edit_note, name='edit_note'),
]
