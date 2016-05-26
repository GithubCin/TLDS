#-*- coding:utf8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50,verbose_name=u"用户")
    password = models.CharField(max_length=50,verbose_name=u"密码")
    sex = models.CharField(max_length=50,verbose_name=u"性别")
    age = models.CharField(max_length=50,verbose_name=u"年龄")
    tel = models.CharField(max_length=50,verbose_name=u"电话")
    email = models.CharField(max_length=50,verbose_name=u"email")
    role_id = models.CharField(max_length=50,verbose_name=u"角色")
    def __unicode__(self):
        return self.username
class Role(models.Model):
    role_id =models.ForeignKey(User,related_name='person_id')
    rolename = models.CharField(max_length=50,verbose_name=u"角色名")
