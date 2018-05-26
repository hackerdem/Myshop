from django import forms
from .views import Wishlist
#PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class ProductAddWishlistForm(forms.Form):
    class Meta:
        model=Wishlist
        fields=['userid','productid']
class SearchForm(forms.Form):
    query=forms.CharField()
    