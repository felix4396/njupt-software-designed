# Generated by Django 4.2.11 on 2024-03-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="activaty",
            field=models.CharField(default="跑步", max_length=100),
        ),
    ]
