__author__ = 'vivek.gour'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples-----
    url(r'^tasks/', 'Celery_test.tasks.tasks')
)