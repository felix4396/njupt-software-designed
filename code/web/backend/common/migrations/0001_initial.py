# Generated by Django 4.2.11 on 2024-03-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]
