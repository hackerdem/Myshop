from django import forms
from .views import Wishlist, Product, Color, Size, Category,Room
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html



class FilterForm(forms.Form):
    def feature_choices(class_name):
        return [(i.name.capitalize(),i.name.capitalize()) for i in class_name.objects.all()]
    CHOICES = (('1', 'A'), ('2', 'B'), ('3', 'C'))
    PRICE_CHOICES=[('0-100','0-100$'),('100-200','100-200$'),('200-300','200-300$'),('300-400','300-400'),('400-10000','400+')]
    print(Category.objects.all())
    category = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple(),choices= feature_choices(Category))
    color = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple(),choices= feature_choices(Color))
    size = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple(),choices= feature_choices(Size))
    room = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple(),choices= feature_choices(Room))
    price = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple(),choices=PRICE_CHOICES)
    
    
class ProductAddWishlistForm(forms.Form):
    class Meta:
        model=Wishlist
        fields=['userid','productid']
class SearchForm(forms.Form):
    query=forms.CharField()
    

