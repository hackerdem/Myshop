"""myshop URL Configuration

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
from django.conf import settings
from django.shortcuts import render
from django.conf.urls.static import static
handler404 = 'my_app.views.handler404'

urlpatterns = [
    url(r'^aboutus/',lambda request: render(request,'aboutus.html')),
    url(r'^contact/',include('contact.urls',namespace='contact')),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('payment.urls',namespace='payment')),
    url(r'^cart/',include('cart.urls',namespace='cart')),
    url(r'^account/',include('account.urls',namespace='account')),
    url(r'^coupons/',include('coupons.urls',namespace='coupons')),
    url(r'^shop/',include('shop.urls',namespace='shop')),
    url('social-auth/',include('social.apps.django_app.urls',namespace='social')),
    url(r'^',include('shop.urls',namespace='shop')),#fix this later shop namespace in two urls
    url(r'^purchases/',include('purchases.urls',namespace='purchases')),
    url(r'^adminosmagnificos/',admin.site.urls),
]
if settings.DEBUG==True:
    urlpatterns+=static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)