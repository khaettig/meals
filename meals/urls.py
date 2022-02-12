from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("recipes/", include("recipes.urls", namespace="recipes")),
    path("admin/", admin.site.urls),
]
