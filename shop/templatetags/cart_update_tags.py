from django import template
from shop.models import Color,Size,Room,Category,Image
from cart.cart import Cart
register=template.Library()


@register.inclusion_tag('cart.html',takes_context=True)
def show_cart(context):
    request = context['request']
    cart=Cart(request)
    return {'cart':cart,'product':request}