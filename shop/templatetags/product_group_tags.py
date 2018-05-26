from django import template
from shop.models import Color,Size,Room,Category,Image
register=template.Library()


@register.inclusion_tag('menu.html',takes_context=True)
def show_menu(context):
    request = context['request']
    categories=Category.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
    rooms=Room.objects.all()
    features={'color':colors,'room':rooms,'size':sizes,'category':categories}
    return {'features':features,'request':request}


@register.inclusion_tag('slidergallery.html',takes_context=True)
def show_images(context):
    product=context['product']
    images=Image.objects.filter(product=product)
    return {'imagest':images}

@register.inclusion_tag('mainimage.html',takes_context=True)
def get_main_image(context):
    product=context['product']
    image=Image.objects.filter(product=product).filter(main_image=True)
    return {'image':image}

@register.inclusion_tag('shoplistfilter.html',takes_context=True)
def get_filter_features(context):
    features=context['features']
    
    return {'features':features}