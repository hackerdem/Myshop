from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^shippinginfo/$',views.check_user_registration,name='check_user_registration'),
    url(r'^create/$',views.purchase_create,name='purchase_create'),
    url(r'^admin/purchase/(?P<order_id>\d+)/$',views.admin_purchase_detail,name='admin_purchase_detail'),
    url(r'^admin/purchase/(?P<purchase_id>\d+)/pdf/$',views.admin_purchase_pdf,name='admin_order_pdf'),
]