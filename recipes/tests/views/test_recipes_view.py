from django.shortcuts import reverse
from django.test import TestCase

from core.factories import RecipeFactory, UserFactory


class RecipesViewTest(TestCase):
    def test_redirects_anonymous_users(self):
        response = self.client.get(reverse("recipes:recipes"))

        self.assertEqual(response.status_code, 302)

    def test_renders_correct_template(self):
        UserFactory(logged_in_to=self.client)

        response = self.client.get(reverse("recipes:recipes"))

        self.assertTemplateUsed(response, "recipes/recipes.html")

    def test_can_sort_by_descending_name(self):
        UserFactory(logged_in_to=self.client)
        recipes = RecipeFactory.create_batch(3)

        response = self.client.get(reverse("recipes:recipes") + "?ordering=-name")

        self.assertEqual(
            list(response.context["recipes"]),
            [recipes[2], recipes[1], recipes[0]],
        )

    def test_can_filter_by_name(self):
        UserFactory(logged_in_to=self.client)
        recipes = RecipeFactory.create_batch(3)

        response = self.client.get(reverse("recipes:recipes") + "?filter=0")
        self.assertEqual(
            list(response.context["recipes"]),
            [recipes[0]],
        )
