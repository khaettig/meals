from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View


class HomeView(LoginRequiredMixin, View):
    pass
