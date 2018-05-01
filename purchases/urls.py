from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^shippinginfo/$',views.check_user_registration,name='check_user_registration'),
    url(r'^create/$',views.purchase_create,name='purchase_create'),
]