from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    url(r'^', include('apps.d_ninjas.urls')),	# use your app_name here
]