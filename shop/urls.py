
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^latest/$',views.product_latest,name='product_latest'),
    url(r'^all/$',views.product_list,name='product_list'),
    url(r'^most_viewed/$',views.product_most_viewed,name='product_most_viewed'),
    url(r'^$',views.product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]

