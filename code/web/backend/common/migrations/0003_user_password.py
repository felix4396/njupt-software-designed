# Generated by Django 4.2.11 on 2024-03-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_data_terminal"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="", max_length=100),
        ),
    ]