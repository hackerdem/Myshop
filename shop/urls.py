
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^filter/(?P<slug>[-\w]+)/$',views.size_color_room_filter,name='size_color_room_filter'),
    url(r'^latest/$',views.product_latest,name='product_latest'),
    url(r'^all/$',views.product_list,name='product_list'),
    url(r'^most_viewed/$',views.product_most_viewed,name='product_most_viewed'),
    url(r'^$',views.product_list,name='product_list'),
    
    url(r'^(?P<slug>[-\w]+)/(?P<name>[-\w]+)/$',views.product_list_by_feature,name='product_list_by_feature'),
    url(r'^(?P<room_slug>[-\w]+)/$',views.product_list_by_feature,name='product_list_by_feature'),
    url(r'^(?P<size_slug>[-\w]+)/$',views.product_list_by_feature,name='product_list_by_feature'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]

