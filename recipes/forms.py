from django import forms


class AddRecipeForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 80}), required=False
    )
    url = forms.URLField(required=False)