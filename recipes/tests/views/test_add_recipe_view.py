from django.shortcuts import reverse
from django.test import TestCase

from core.factories import UserFactory


def invalid_data():
    return {}


def valid_data():
    return {"name": "Name"}


class AddRecipeViewTest(TestCase):
    def test_redirects_anonymous_users(self):
        response = self.client.get(reverse("recipes:add_recipe"))

        self.assertEqual(response.status_code, 302)

    def test_renders_correct_template(self):
        UserFactory(logged_in_to=self.client)

        response = self.client.get(reverse("recipes:add_recipe"))

        self.assertTemplateUsed(response, "recipes/add_recipe.html")

    def test_invalid_post_renders_page_again(self):
        UserFactory(logged_in_to=self.client)

        response = self.client.post(reverse("recipes:add_recipe"), invalid_data())

        self.assertTemplateUsed(response, "recipes/add_recipe.html")

    def test_valid_post_redirects(self):
        UserFactory(logged_in_to=self.client)

        response = self.client.post(reverse("recipes:add_recipe"), valid_data())

        self.assertEqual(response.status_code, 302)
