from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^configure$', views.configure),
    url(r'^add$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update)
]