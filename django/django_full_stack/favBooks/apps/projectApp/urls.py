from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^home_dashboard$', views.home_dashboard),
    url(r'^userList/(?P<member_id>\d+)$', views.userList),
    url(r'^addBook/(?P<id>\d+)$', views.addBook),
    url(r'^bookDesc/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.bookDesc),
    url(r'^update/(?P<book_id>\d+)/(?P<id>\d+)$', views.update),
    url(r'^deleteDesc/(?P<book_id>\d+)/(?P<id>\d+)$', views.deleteDesc),
    url(r'^addFav/(?P<book_id>\d+)/(?P<id>\d+)$', views.addFav),
    url(r'^removeFav/(?P<book_id>\d+)/(?P<id>\d+)$', views.removeFav)
]