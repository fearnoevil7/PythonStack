from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^transactions$', views.transactions),
    url(r'^clear$', views.clear),
]