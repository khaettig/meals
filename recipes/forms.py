from django import forms

from core.mixins import FormExceptionHandlerMixin
from recipes.models import Category, Recipe
from recipes.services import RecipeAlreadyExists


class RecipeForm(FormExceptionHandlerMixin, forms.Form):
    handled_exceptions = {
        RecipeAlreadyExists: ("name", "A recipe with this name already exists!")
    }

    recipe_fields = forms.fields_for_model(Recipe)
    name = recipe_fields["name"]
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 20}), required=False
    )
    category_id = forms.ChoiceField(label="Category")
    url = recipe_fields["url"]

    def __init__(self, *args, **kwargs):
        self.base_fields["category_id"].choices = (
            (c.id, c.name) for c in Category.objects.all().order_by("id")
        )
        super().__init__(*args, **kwargs)
