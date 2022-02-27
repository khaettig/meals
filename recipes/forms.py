from django import forms


class AddRecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 20}), required=False
    )
    url = forms.URLField(required=False)
