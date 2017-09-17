from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    cart_list=CartInfo.objects.filter(user_id=1)#request.session['uid']
    context={'clist':cart_list}
    return render(request,'tt_cart/cart.html',context)
'''
http://127.0.0.1:8000/order/?cid=2&cid=3
http://127.0.0.1:8000/order/?cid=1&cid=2
'''