"""assignment5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from assignment5 import settings
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('', views.index, name="index"),
    path('login_sign/', views.login_sign, name="login_sign"),
    path('services/', views.services, name="services"),
    path('register/', views.register, name="register"),
    path('loginuser/', views.loginuser, name="loginuser"),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
    path('quiz/', views.quiz, name="quiz"),
    path('submit_test/', views.submit_test, name="submit_test"),
]
