"""
URL configuration for SpecificTemplates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Static URL Suffixes(Normal URLs)
    path('SchoolList/',SchoolList.as_view(),name='SchoolList'),
    path('StudentList/',StudentList.as_view(),name='StudentList'),
    path('SchoolCreate/',SchoolCreate.as_view(),name='SchoolCreate'),
    path('StudentCreate/',StudentCreate.as_view(),name='StudentCreate'),

    # Dynamic URL Suffixes(Canonical URLs)
    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='SchoolDetail'),
    re_path('(?P<name>\d+)/',StudentDetail.as_view(),name='StudentDetail'),
]
