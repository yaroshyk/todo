from django.contrib import admin

from django.urls import path

from api import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<int:item_id>', views.remove, name="del"),
    path('admin', admin.site.urls),
    path('add', views.add, name="add")
]
