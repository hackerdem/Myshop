from django import forms
from .views import Wishlist, Product, Color, Size, Category
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html
#PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class FeatureGroupSelect(forms.widgets.Select):
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        class_attr = ''
        return format_html('<option value="{0}"{1} class="{3}">{2}</option>',
        option_value,
        selected_html,
        force_text(option_label),
        class_attr)
class FeatureModelChoicesField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = FeatureGroupSelect
        super(FeatureModelChoicesField,self).__init__( *args, **kwargs)

class FilterForm(forms.Form):
    categorygroup_id = FeatureModelChoicesField(queryset = Category.objects.all())
class ProductAddWishlistForm(forms.Form):
    class Meta:
        model=Wishlist
        fields=['userid','productid']
class SearchForm(forms.Form):
    query=forms.CharField()
    

