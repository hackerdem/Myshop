from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^shippinginfo/$',views.purchase_create,name='purchase_create'),
    url(r'^create/$',views.purchase_create,name='purchase_create'),
]