# Generated by Django 1.11.dev20161105150738 on 2016-11-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_corporatemember_django_usage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="corporatemember",
            name="django_usage",
            field=models.TextField(blank=True, help_text="Not displayed publicly."),
        ),
    ]
