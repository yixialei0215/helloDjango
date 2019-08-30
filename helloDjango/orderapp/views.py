from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def order_list(request, order_num, city_code):
    print(order_num, city_code)
    return render(request,
                  'list_order.html',
                  locals())


def cencel_order(request, order_num):
    # order_num订单编号是UUID类型
    print()
    return render(request,
                  'list_order.html',
                  locals())


def search(request, phone):
    return HttpResponse('phone:%s' % phone)


def query(request):
    # 查询参数中code
    # (1:按城市city和订单号num查询
    #  2:按手机号phone查询)
    # url = reverse('order:search',
    #               args=('17791692077',))
    # return redirect(url)
    url = reverse('order:list', kwargs={'city_code': 'XA', 'order_num': 1009})
    return HttpResponseRedirect(url)
    # return HttpResponse('h1,Query %s ' % url)
