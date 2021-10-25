from django.contrib.auth import views as base_auth_views
from django.urls import path, include
from authentication import views as auth_views

urlpatterns = [
    path('accounts/login/', base_auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('accounts/logout/', base_auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', auth_views.register, name="register"),
]
