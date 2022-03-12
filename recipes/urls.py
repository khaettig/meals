from django.urls import path

from recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.RecipesView.as_view(), name="recipes"),
    path("<int:recipe_id>/", views.RecipeView.as_view(), name="recipe"),
    path("add/", views.AddRecipeView.as_view(), name="add_recipe"),
]
