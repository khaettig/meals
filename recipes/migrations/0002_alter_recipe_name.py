# Generated by Django 4.0.1 on 2022-02-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
