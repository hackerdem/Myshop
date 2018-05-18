from django import template
from shop.models import Color,Size,Room,Category
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