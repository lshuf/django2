from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cart_add/$',views.cart_add),

    #
    url(r'^detail/$',views.detail)
]