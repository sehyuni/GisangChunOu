"""GisangChun URL Configuration

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
from django.contrib import admin
from django.urls import path
import home.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_mem/', home.views.home_mem, name='home_mem'),
    path('home/', home.views.home),
    path('', home.views.index),
    path('login/', home.views.login),
    path('mypage/', home.views.mypage),
    path('newmember/', home.views.newmember),
    path('ranking/', home.views.ranking),
    path('forecast/', home.views.forecast, name='forecast')
]
