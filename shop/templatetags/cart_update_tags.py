from django import template
from shop.models import Color,Size,Room,Category,Image
from cart.cart import Cart
from shop.views import Wishlist
register=template.Library()


@register.inclusion_tag('cart.html',takes_context=True)
def show_cart(context):
    request = context['request']
    cart=Cart(request)
    
    return {'cart':cart,}

@register.inclusion_tag('wishlist.html',takes_context=True)
def show_wishlist(context):
    request = context['request']

    if request.user.is_authenticated:
        wishlist=Wishlist.objects.filter(userid=request.user)
    else:
        #wishlist=Wishlist.objects.all()
        wishlist=[]
    return {'wishlist':wishlist,}