from __future__ import unicode_literals
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import ContactUsView

app_name='contact'
urlpatterns=[
    url(r'^$',ContactUsView.as_view(),{},'contact'),
    url(r'^success/$',TemplateView.as_view(template_name='contact/contact_success.html'),{},'contact-success'),
]