"""Db_connect URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from AppConnectDb import views

urlpatterns = [
    path('', views.index),
    re_path(r'create/$', views.create), # re_path - регулярное выражение, чтобы найти create/ в любом случае
    re_path(r'back/$', views.back), # возврат на главную стрницу.
    re_path(r'buy/$', views.buy),  # возврат на главную стрницу.
    re_path(r'save/$', views.save),  # возврат на главную стрницу.
    # re_path(r'getlist/$', views.getlist)  # возврат на главную стрницу.

]