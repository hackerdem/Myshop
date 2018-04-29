from django import forms
from .models import Order
from django.db import models

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['shipping_first_name','shipping_last_name',
                'shipping_email','shipping_address',
                'shipping_landmark','shipping_country',
                'shipping_state','shipping_city','shipping_postcode',
                'billing_first_name','billing_last_name',
                'billing_email','billing_address',
                'billing_landmark','billing_country',
                'billing_state','billing_city','billing_postcode',
                'use_shipping_for_billing',

        ]

