#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from distribution.models import *
# Create your views here.

#表单
class OrderForm(forms.Form):
    destn = forms.CharField(label='目的地',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    node_id = forms.CharField(label='配送地',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    acceptdate = forms.CharField(label='收寄日期',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    user_id = forms.CharField(label='寄件人',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    accepter = forms.CharField(label='收件人',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    accepterphonenumber = forms.CharField(label='收件人电话号码',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.CharField(label='价格',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    scope = forms.CharField(label='配送范围',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    senddate = forms.CharField(label='发送日期',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='收件人地址',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    mateprice = forms.CharField(label='配送价格',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    totalprice = forms.CharField(label='总价格',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))



def index (request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html', {'username':username},context_instance=RequestContext(request))
def orderadd(request):
    if request.method == 'POST':
        uf = OrderForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            destn = uf.cleaned_data['destn']
            node_id = uf.cleaned_data['node_id']
            acceptdate = uf.cleaned_data['acceptdate']
            user_id = uf.cleaned_data['user_id']
            accepter = uf.cleaned_data['accepter']
            accepterphonenumber = uf.cleaned_data['accepterphonenumber']
            price = uf.cleaned_data['price']
            scope = uf.cleaned_data['scope']
            senddate = uf.cleaned_data['senddate']
            address = uf.cleaned_data['address']
            mateprice = uf.cleaned_data['mateprice']
            totalprice = uf.cleaned_data['totalprice']
            #添加到数据库
            Order.objects.create(destn= destn,node_id=node_id,acceptdate= acceptdate,user_id= user_id,accepterphonenumber= accepterphonenumber,price= price,scope= scope,senddate= senddate,address= address,mateprice= mateprice,totalprice= totalprice,accepter=accepter)
            messages = 'success'
            return HttpResponseRedirect('/order_add')
    else:
        messages = ''
        uf = OrderForm()
    return render_to_response('order_add.html',{'uf':uf,'messages':messages}, context_instance=RequestContext(request))

def orderlist (request):
    orderlist = Order.objects.all()
    return render_to_response('order_list.html', {'orderlist':orderlist},context_instance=RequestContext(request))
