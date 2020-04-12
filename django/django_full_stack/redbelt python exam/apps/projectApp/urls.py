from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^home_dashboard$', views.home_dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create_thought/(?P<id>\d+)$', views.create_thought),
    url(r'^thought_desc/(?P<thought_id>\d+)/(?P<user_id>\d+)$', views.thought_desc),
    url(r'^addLike/(?P<thought_id>\d+)/(?P<user_id>\d+)$', views.addLike),
    url(r'^unlike/(?P<thought_id>\d+)/(?P<user_id>\d+)$', views.unlike),
    url(r'^delete/(?P<thought_id>\d+)/(?P<user_id>\d+)$', views.delete),
]