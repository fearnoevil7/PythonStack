from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^postMessage$', views.postMessage),
    url(r'^postComment/(?P<id>\d+)$', views.postComment)
]