from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe


class AddRecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 20}), required=False
    )
    url = forms.URLField(required=False)

    def clean_name(self):
        if Recipe.objects.filter(name=self.cleaned_data["name"]).exists():
            raise ValidationError("A recipe with that name already exists!")
        return self.cleaned_data["name"]
