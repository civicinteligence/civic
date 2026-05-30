from django.urls import path
from .views import register, office_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', register, name='register'),
    path("login", office_login, name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]