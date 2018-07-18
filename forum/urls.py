"""Defines URL patterns for tasks."""


from django.conf.urls import url
from . import views


urlpatterns = [


    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/(?P<question_id>\d+)/$', views.question, name='question'),
    url(r'^new_question/$', views.new_question, name='new_question'),
    url(r'^new_comment/(?P<question_id>\d+)/$', views.new_comment, name='new_comment'),
    url(r'^edit_comment/(?P<comment_id>\d+)/$',views.edit_comment, name='edit_comment'),
]
