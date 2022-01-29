from django.urls import path

from recipes import views

app_name = "recipes"

urlpatterns = [
    path("add_recipe/", views.AddRecipeView.as_view(), name="add_recipe"),
]
