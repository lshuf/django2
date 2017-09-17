"""ttsx_sz2 URL Configuration

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
    url('^user/',include('tt_user.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url('^cart/',include('tt_cart.urls')),
    url('^order/',include('tt_order.urls')),
    url('^',include('tt_goods.urls')),
url(r'^pc-geetest/register', 'app.views.pcgetcaptcha', name='pcgetcaptcha'),
    url(r'^mobile-geetest/register', 'app.views.mobilegetcaptcha', name='mobilegetcaptcha'),
    url(r'^pc-geetest/validate$', 'app.views.pcvalidate', name='pcvalidate'),
    url(r'^pc-geetest/ajax_validate','app.views.pcajax_validate', name='pcajax_validate'),
    url(r'^mobile-geetest/ajax_validate','app.views.mobileajax_validate', name='mobileajax_validate'),
    url(r'^lsf/', 'app.views.home', name='home'),
]
