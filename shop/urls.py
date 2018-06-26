
from django.conf.urls import url
from django.urls import path
from . import views

app_name='shop'
urlpatterns=[
    url(r'^ajax/',views.wishlist_add_ajax,name='wishlist_add_ajax'),
    url(r'^product_listing/$', views.product_listing, name = 'product_listing'),
    url(r'^$',views.product_list,name='product_list'),
    url(r'^wishlist/$',views.show_wishlist,name='show_wishlist'),
    url(r'^add_to_wishlist/(?P<product_id>\d+)/$',views.add_to_wishlist,name='add_to_wishlist'),
    url(r'^remove_wishlist_item/(?P<product_id>\d+)/$',views.remove_wishlist_item,name='remove_wishlist_item'),
    url(r'^product_listing/$',views.product_listing,name='product_listing'),
    url(r'^filter/(?P<slug>[-\w]+)/$',views.product_list,name='size_color_room_filter'),
    url(r'^latest/$',views.product_list,name='product_latest'),
    url(r'^all/$',views.product_list,name='product_list'),
    url(r'^most_viewed/$',views.product_list,name='product_most_viewed'),
    url(r'^shop_list/$',views.product_list,name='collection_shop_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
    url(r'^(?P<slug>[-\w]{,8})/(?P<name>[-\w]+)/$',views.product_list,name='product_list_by_feature'),

]

