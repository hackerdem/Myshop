from django.conf.urls import url
from . import views
app_name='cart'
urlpatterns=[
    url(r'^$',views.cart_detail,name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$',views.cart_add,name='cart_add'),
    url(r'^ajax/',views.cart_add_ajax,name='cart_add_ajax'),
    url(r'^remove/(?P<product_id>\d+)/$',views.cart_remove,name='cart_remove'),
    url(r'^carttotal/$',views.carttotal,name='carttotal'),
    url(r'^product_custom_filter/$',views.product_custom_filter,name='product_custom_filter'),
]

