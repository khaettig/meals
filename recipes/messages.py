from django.contrib import messages


def add_recipe_created_message(request):
    messages.add_message(
        request, messages.INFO, "Your recipe was created!", extra_tags="success"
    )


def add_recipe_saved_message(request):
    messages.add_message(
        request, messages.INFO, "Your recipe was saved!", extra_tags="success"
    )
