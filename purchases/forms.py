from django import forms
from .models import Purchase

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields=['shipping_first_name','shipping_last_name','shipping_email','shipping_address',
                'shipping_landmark','shipping_country','shipping_state','shipping_city','shipping_postcode',
                'billing_first_name','billing_lastname','billing_email','billing_address','billing_landmark',
                'billing_country','billing_state','billing_city','billing_postcode','use_shipping_for_billing'
        ]