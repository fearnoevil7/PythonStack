from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home(?P<page>\w+)$', views.index),
    url(r'^(?P<page>\w+)/process$', views.process),
    url(r'^(?P<page>\w+)/description/(?P<id>\d+)$', views.description),
    url(r'^(?P<page>\w+)/append/(?P<id>\d+)$', views.append)
]