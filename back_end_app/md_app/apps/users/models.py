from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """用户模型类"""

    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        db_table = 'db_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class UserInfo(models.Model):
    """用户生日"""
    birthday = models.DateField(null=True, verbose_name='生日')
    gender = models.CharField(max_length=5, choices=(('male', u'男'), ('female', u'女')), default='female')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_userinfo'
