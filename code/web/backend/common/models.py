from django.db import models


# Create your models here.
class User(models.Model):
    # 用户名称
    name = models.CharField(max_length=100)

    password = models.CharField(max_length=100, default='')

    phone_number = models.CharField(max_length=15)

    address = models.CharField(max_length=100)


class Terminal(models.Model):
    terminal_id = models.CharField(max_length=100)

    terminal_ip = models.CharField(max_length=15)


class Data(models.Model):
    blood_oxygen = models.CharField(max_length=5)

    user_name = models.CharField(max_length=100)

    terminal_id = models.CharField(max_length=100)

    time_stamp = models.DateTimeField()
