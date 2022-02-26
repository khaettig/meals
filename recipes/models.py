from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    url = models.URLField(null=True)
