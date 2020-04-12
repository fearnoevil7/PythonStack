"""tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from tasksApp.views import task, show, usr, session
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include
from rest_framework.authtoken import views
from  rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# from rest_framework import routers
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('task', task.as_view()),
    path('task/<int:task_id>', show.as_view()),
    path('user', usr.as_view()),
    # path('api/', include('tasksApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('session', session.as_view()),
    # path(r'api-token-refresh/', refresh_auth_token),
]
