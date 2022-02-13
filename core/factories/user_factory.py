from django.contrib.auth import get_user_model
from factory import post_generation
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = "username"

    @post_generation
    def password(user, _, password):
        user.set_password(password if password else "password")
