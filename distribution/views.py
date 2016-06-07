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

class TabaccoForm(forms.Form):
    tobacconame = forms.CharField(label='烟草名称',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    unitprice = forms.CharField(label='烟草单价',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

class StateForm(forms.Form):
    bagnum = forms.CharField(label='封装袋号',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    order_id = forms.CharField(label='订单号',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    nowposition = forms.CharField(label='当前地点',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    nextposition = forms.CharField(label='下一目的地',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    arrivetime = forms.CharField(label='到达时间',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))


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

def orderupdate(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    order = Order.objects.get(id=offset)
    if request.method == 'POST':
        uf = OrderForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            order.destn = uf.cleaned_data['destn']
            order.node_id = uf.cleaned_data['node_id']
            order.acceptdate = uf.cleaned_data['acceptdate']
            order.user_id = uf.cleaned_data['user_id']
            order.accepter = uf.cleaned_data['accepter']
            order.accepterphonenumber = uf.cleaned_data['accepterphonenumber']
            order.price = uf.cleaned_data['price']
            order.scope = uf.cleaned_data['scope']
            order.senddate = uf.cleaned_data['senddate']
            order.address = uf.cleaned_data['address']
            order.mateprice = uf.cleaned_data['mateprice']
            order.totalprice = uf.cleaned_data['totalprice']
            order.save()
            messages = 'success'
            return HttpResponseRedirect('/order_list')
    else:
        messages = ''
        uf = OrderForm(initial={'destn': order.destn,'node_id': order.node_id,'acceptdate': order.acceptdate,'user_id': order.user_id,'accepter': order.accepter,'accepterphonenumber': order.accepterphonenumber,'price': order.price,'scope': order.scope,'senddate': order.senddate,'address': order.address,'mateprice': order.mateprice,'totalprice': order.totalprice, })

    return render_to_response('order_update.html',{'uf':uf,'order':order}, context_instance=RequestContext(request))
def orderdelete(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    order = Order.objects.get(id=offset)
    order.delete()
    return HttpResponseRedirect('/order_list')

def tobaccoGoodadd(request):
    if request.method == 'POST':
        uf = TabaccoForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            tobacconame = uf.cleaned_data['tobacconame']
            unitprice = uf.cleaned_data['unitprice']
            #添加到数据库
            TobaccoGood.objects.create(tobacconame= tobacconame,unitprice=unitprice)
            messages = 'success'
            return HttpResponseRedirect('/tobaccoGood_add')
    else:
        messages = ''
        uf = TabaccoForm()
    return render_to_response('tobacco_add.html',{'uf':uf,'messages':messages}, context_instance=RequestContext(request))
def tobaccoGoodlist (request):
    tabaccolist = TobaccoGood.objects.all()
    return render_to_response('tobacco_list.html', {'tabaccolist':tabaccolist},context_instance=RequestContext(request))
def tobaccoGoodupdate(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    tobaccoGood = TobaccoGood.objects.get(id=offset)
    if request.method == 'POST':
        uf = TabaccoForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            tobaccoGood.tobacconame = uf.cleaned_data['tobacconame']
            tobaccoGood.unitprice = uf.cleaned_data['unitprice']
            tobaccoGood.save()
            messages = 'success'
            return HttpResponseRedirect('/tobaccoGood_list')
    else:
        messages = ''
        uf = TabaccoForm(initial={'tobacconame': tobaccoGood.tobacconame,'unitprice': tobaccoGood.unitprice, })

    return render_to_response('tobacco_update.html',{'uf':uf,}, context_instance=RequestContext(request))
def tobaccoGooddelete(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    tobaccoGood = TobaccoGood.objects.get(id=offset)
    tobaccoGood.delete()
    return HttpResponseRedirect('/tobaccoGood_list')


def stateadd(request):
    if request.method == 'POST':
        uf = StateForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            bagnum = uf.cleaned_data['bagnum']
            order_id = uf.cleaned_data['order_id']
            nowposition = uf.cleaned_data['nowposition']
            nextposition = uf.cleaned_data['nextposition']
            arrivetime = uf.cleaned_data['arrivetime']
            #添加到数据库
            GoodState.objects.create(bagnum= bagnum,order_id=order_id,nowposition= nowposition,nextposition= nextposition,arrivetime= arrivetime,)
            messages = 'success'
            return HttpResponseRedirect('/state_add')
    else:
        messages = ''
        uf = StateForm()
    return render_to_response('state_add.html',{'uf':uf,'messages':messages}, context_instance=RequestContext(request))
def statelist (request):
    statelist = GoodState.objects.all()
    return render_to_response('state_list.html', {'statelist':statelist},context_instance=RequestContext(request))
def stateupdate(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    goodState = GoodState.objects.get(id=offset)
    if request.method == 'POST':
        uf = StateForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            goodState.bagnum = uf.cleaned_data['bagnum']
            goodState.order_id = uf.cleaned_data['order_id']
            goodState.nowposition = uf.cleaned_data['nowposition']
            goodState.nextposition = uf.cleaned_data['nextposition']
            goodState.arrivetime = uf.cleaned_data['arrivetime']
            goodState.save()
            messages = 'success'
            return HttpResponseRedirect('/state_list')
    else:
        messages = ''
        uf = StateForm(initial={'bagnum': goodState.bagnum,'order_id': goodState.order_id, 'nowposition': goodState.nowposition,'nextposition': goodState.nextposition,'arrivetime': goodState.arrivetime,})

    return render_to_response('state_update.html',{'uf':uf,}, context_instance=RequestContext(request))
def statedelete(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    statelist = GoodState.objects.get(id=offset)
    statelist.delete()
    return HttpResponseRedirect('/state_list')

