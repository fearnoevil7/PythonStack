from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^user_dashboard$', views.user_dashboard),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^bookDesc/(?P<id>\d+)$', views.bookDesc),
    url(r'^addHome/(?P<id>\d+)$', views.addHome),
    url(r'^userDesc/(?P<id>\d+)$', views.userDesc),
    url(r'^addReview/(?P<id>\d+)$', views.addReview),
    url(r'^deleteReview/(?P<review_id>\d+)/(?P<user_id>\d+)/(?P<book_id>\d+)$', views.deleteReview),

]