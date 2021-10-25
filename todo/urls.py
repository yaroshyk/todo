from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import views
from authentication import urls as auth_urls

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<int:item_id>', views.remove, name="del"),
    path('admin', admin.site.urls),
    path('add', views.add, name="add"),
    path('edit/<int:item_id>', views.edit, name="edit"),
    path('', include(auth_urls)),
]
