#-*- coding:utf8 -*-
from django.db import models

# Create your models here.
#线路表
class Route(models.Model):
    routename = models.CharField(max_length=50,verbose_name=u"路线名称")
    routefrom = models.CharField(max_length=50,verbose_name=u"始发点")
    routeto= models.CharField(max_length=50,verbose_name=u"终点")
#路线关系
class RouteRelation(models.Model):
    node_id = models.CharField(max_length=50,verbose_name=u"配送点")
    route_id = models.CharField(max_length=50,verbose_name=u"路线")
#货物状态
class GoodState(models.Model):
    bagnum = models.CharField(max_length=50,verbose_name=u"封装袋号")
    order_id = models.CharField(max_length=50,verbose_name=u"订单号")
    nowposition = models.CharField(max_length=50,verbose_name=u"当前地点")
    nextposition = models.CharField(max_length=50,verbose_name=u"下一目的地")
    arrivetime = models.CharField(max_length=50,verbose_name=u"到达时间")
class TobaccoGood(models.Model):
    tobacconame = models.CharField(max_length=50,verbose_name=u"烟草名称")
    unitprice = models.CharField(max_length=50,verbose_name=u"烟草单价")
class Order(models.Model):
    destn = models.CharField(max_length=50,verbose_name=u"目的地")
    node_id = models.CharField(max_length=50,verbose_name=u"配送地")
    acceptdate = models.CharField(max_length=50,verbose_name=u"收寄日期")
    user_id = models.CharField(max_length=50,verbose_name=u"寄件人")
    accepter = models.CharField(max_length=50,verbose_name=u"收件人")
    accepterphonenumber = models.CharField(max_length=50,verbose_name=u"收件人电话号码")
    price = models.CharField(max_length=50,verbose_name=u"价格")
    scope = models.CharField(max_length=50,verbose_name=u"配送范围")
    senddate = models.CharField(max_length=50,verbose_name=u"发送日期")
    address = models.CharField(max_length=50,verbose_name=u"收件人地址")
    mateprice = models.CharField(max_length=50,verbose_name=u"配送价格")
    totalprice = models.CharField(max_length=50,verbose_name=u"总价格")
class OrderContent(models.Model):
    order = models.ForeignKey(Order,related_name='order_name')
    tobaccoGood = models.ForeignKey(TobaccoGood,related_name='tobacco_name')
    tobacconum = models.CharField(max_length=50,verbose_name=u"数量")
