from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('api.urls'))
]
