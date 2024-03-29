from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        "recipes.Category", on_delete=models.SET_DEFAULT, default=0
    )

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"
