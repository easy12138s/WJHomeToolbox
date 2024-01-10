
# Create your models here.

from django.db import models

# Create your models here.

class HomeUsers(models.Model):
    account = models.CharField(max_length=30)  # 账号
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=12, null=True)  # 性别
    head_dic = models.CharField(max_length=255, null=True)  # 头像
    status = models.CharField(max_length=1)  # 状态 1为启用 0为停用

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ('account',)
