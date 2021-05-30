from django.contrib import admin

from django.urls import path

from api import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del', views.remove, name="del"),
    path('admin', admin.site.urls)
]
