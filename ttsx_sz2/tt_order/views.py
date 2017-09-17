from django.shortcuts import render,redirect
from .models import *
from tt_cart.models import CartInfo
from django.db import transaction
from datetime import datetime
# Create your views here.
def index(request):
    cid=request.GET.getlist('cid')#[1,2]
    cart_list=CartInfo.objects.filter(id__in=cid)
    context={'clist':cart_list}
    return render(request,'tt_order/order.html',context)
def buy_now(request):
    pass
    '''
    请求的数据包括：商品的id、数量
    根据id查询出来商品对象
    context={'goods':goods,'count':count}
    '''
'''
http://127.0.0.1:8000/order/?cid=1&cid=2
'''

'''
创建订单主表
查询选中的购物车信息，逐个遍历
判断商品库存是否满足当前购买数量
如果库存量不足，则事务回滚，转到购物车页面
如果库存量足够，则减少库存量，创建详单对象，删除购物车对象
计算总金额，循环结束后存储
'''
@transaction.atomic
def do_order(request):
    #接收请求的数据
    cid=request.POST.getlist('cid')
    #开启事务
    sid=transaction.savepoint()
    #创建订单主表
    order=OrderInfo()
    order.oid='%s%d'%(datetime.now().strftime('%Y%m%d%H%M%S'),1)
    order.user_id=1
    order.ototal=0
    order.oaddress=''
    order.save()
    #查询选中的购物车信息，逐个遍历
    isok=True
    total=0
    cart_list=CartInfo.objects.filter(id__in=cid)
    for cart in cart_list:
        #判断商品库存是否满足当前购买数量
        if cart.count<=cart.goods.gkucun:
            #如果库存量足够
            #计算总金额
            total+=cart.count*cart.goods.gprice
            #减少库存量
            cart.goods.gkucun-=cart.count
            cart.goods.save()
            #创建详单对象
            detail=OrderDetailInfo()
            detail.goods=cart.goods
            detail.order=order
            detail.price=cart.goods.gprice
            detail.count=cart.count
            detail.save()
            #删除购物车对象
            cart.delete()
        else:
            #如果库存量不足
            isok=False
            break
    if isok:
        #保存总价
        order.ototal=total
        order.save()
        #提交事务
        transaction.savepoint_commit(sid)

        return redirect('/user/order/')
    else:
        #回滚事务
        transaction.savepoint_rollback(sid)

        return redirect('/cart/')




