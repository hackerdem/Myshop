from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^dashboard/$',views.user_dashboard,name='user_dashboard'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^register/$',views.user_register,name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]