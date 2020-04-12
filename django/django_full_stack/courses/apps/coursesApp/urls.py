from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add),
    url(r'^delete/(?P<course_id>\d+)/(?P<description_id>\d+)$', views.delete),
    url(r'^desc/(?P<course_id>\d+)/(?P<description_id>\d+)$', views.desc)
]