from django.contrib import admin

from recipes.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)
