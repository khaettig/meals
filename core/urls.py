from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="core/auth/login.html"),
        name="login",
    ),
]
