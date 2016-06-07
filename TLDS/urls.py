"""TLDS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cuser/', include('cuser.urls')),
    url(r'^$', 'distribution.views.index'),
    url(r'^index/', 'distribution.views.index'),
    url(r'^order_add/', 'distribution.views.orderadd'),
    url(r'^order_list/', 'distribution.views.orderlist'),
    url(r'^order_update/(\d{1,6})/$', 'distribution.views.orderupdate'),
    url(r'^order_delete/(\d{1,6})/$', 'distribution.views.orderdelete'),
    url(r'^tobaccoGood_add/', 'distribution.views.tobaccoGoodadd'),
    url(r'^tobaccoGood_list/', 'distribution.views.tobaccoGoodlist'),
    url(r'^tobaccoGood_update/(\d{1,6})/$', 'distribution.views.tobaccoGoodupdate'),
    url(r'^tobaccoGood_delete/(\d{1,6})/$', 'distribution.views.tobaccoGooddelete'),
    url(r'^state_add/', 'distribution.views.stateadd'),
    url(r'^state_list/', 'distribution.views.statelist'),
    url(r'^state_update/(\d{1,6})/$', 'distribution.views.stateupdate'),
    url(r'^state_delete/(\d{1,6})/$', 'distribution.views.statedelete'),

]
