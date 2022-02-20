from django.shortcuts import reverse
from django.test import TestCase

from core.factories import UserFactory


class RecipesViewTest(TestCase):
    def test_redirects_anonymous_users(self):
        response = self.client.get(reverse("recipes:recipes"))

        self.assertEqual(response.status_code, 302)

    def test_renders_correct_template(self):
        UserFactory(logged_in_to=self.client)

        response = self.client.get(reverse("recipes:recipes"))

        self.assertTemplateUsed(response, "recipes/recipes.html")
