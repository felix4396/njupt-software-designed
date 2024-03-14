from django.db import models


# Create your models here.
class User(models.Model):
    # 用户名称
    name = models.CharField(max_length=100)

    password = models.CharField(max_length=100, default='123456')

    # 1.管理员 2.普通用户
    user_type = models.IntegerField(default=2)

    # phone_number = models.CharField(max_length=15)

    # address = models.CharField(max_length=100)


class Terminal(models.Model):
    terminal_id = models.CharField(max_length=100)

    terminal_ip = models.CharField(max_length=15)


class Data(models.Model):
    blood_oxygen = models.CharField(max_length=20)

    user_name = models.CharField(max_length=100)

    terminal_id = models.CharField(max_length=100)

    time_stamp = models.DateTimeField()

    activity = models.CharField(max_length=100, default='跑步')
