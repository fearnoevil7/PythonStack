from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^home_dashboard$', views.home_dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^bookDescription/(?P<id>\d+)$', views.bookDescription),
    url(r'^addBook$', views.addBook),
    url(r'^addHome/(?P<id>\d+)$', views.addHome),
]