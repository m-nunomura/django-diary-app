"""
URL configuration for mydiaryproject project.

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
from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/",views.IndexView.as_view(),name="index"),
    path("diary/create/",views.DiaryCreateVeiw.as_view(),name="diary_create"),
    path("diary/create/complete/",views.DiaryCreateComplete.as_view(),name="diary_create_complete"),
    path("diary/list/",views.DiaryListView.as_view(),name="diary_list"),
    path("diary/detail/<uuid:pk>",views.DiaryDetailView.as_view(),name="diary_detail"),
]
