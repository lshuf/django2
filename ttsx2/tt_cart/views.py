from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def cart_add(request):
    goods_add = request.POST.get('goods')
    print(goods_add)
    data = {'df':'dsfsd'}

    return JsonResponse(data)

#
def detail(request):
    return render(request,'tt_goods/detail.html')