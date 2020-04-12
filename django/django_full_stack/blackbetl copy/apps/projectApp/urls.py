from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^home_dashboard$', views.home_dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addHome/(?P<user_id>\d+)$', views.addHome),
    url(r'^add/(?P<user_id>\d+)$', views.add),
    url(r'^wishList/(?P<user_id>\d+)$', views.wishList),
    url(r'^addWish/(?P<item_id>\d+)/(?P<user_id>\d+)$', views.addWish),
    url(r'^removeWish/(?P<item_id>\d+)/(?P<user_id>\d+)$', views.removeWish),
    url(r'^delete/(?P<item_id>\d+)/(?P<user_id>\d+)$', views.delete),
    url(r'^descHome/(?P<item_id>\d+)/(?P<user_id>\d+)$', views.descHome),
]