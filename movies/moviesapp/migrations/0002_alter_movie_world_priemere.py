# Generated by Django 5.0.3 on 2024-03-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moviesapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="world_priemere",
            field=models.DateField(default=2019, verbose_name="Премьера в мире"),
        ),
    ]
