from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^log_in$', views.log_in),
    url(r'^success$', views.success),
    url(r'^log_out$', views.log_out)
]