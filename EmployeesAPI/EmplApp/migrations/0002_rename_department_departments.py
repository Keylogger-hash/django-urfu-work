# Generated by Django 5.0.3 on 2024-04-11 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EmplApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Department",
            new_name="Departments",
        ),
    ]