from django.http import HttpResponse
from django.views.generic import View


class AddRecipeView(View):
    def get(self, request):
        return HttpResponse("<title>Add a recipe</title>")
