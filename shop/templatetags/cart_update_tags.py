from django import template
from shop.models import Color,Size,Room,Category,Image
from cart.cart import Cart
register=template.Library()


@register.inclusion_tag('cart.html',takes_context=True)
def show_cart(context):
    request = context['request']
    cart=Cart(request)
    for item in cart:
        #item['image']=Image.objects.filter(product=cart.item['product']).filter(main_image=True)
        print(item)
    return {'cart':cart,}