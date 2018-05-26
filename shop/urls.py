
from django.conf.urls import url

from . import views

app_name='shop'
urlpatterns=[
    url(r'^add_to_wishlist/(?P<product_id>\d+)/$',views.add_to_wishlist,name='add_to_wishlist'),
    url(r'^filter/(?P<slug>[-\w]+)/$',views.size_color_room_filter,name='size_color_room_filter'),
    url(r'^latest/$',views.product_latest,name='product_latest'),
    url(r'^all/$',views.product_list,name='product_list'),
    url(r'^most_viewed/$',views.product_most_viewed,name='product_most_viewed'),
    url(r'^shop_list/$',views.collection_shop_list,name='collection_shop_list'),
    url(r'^$',views.product_list,name='product_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
    url(r'^(?P<slug>[-\w]{,8})/(?P<name>[-\w]+)/$',views.product_list_by_feature,name='product_list_by_feature'),
    
]

