from django import template
from shop.models import Color,Size,Room,Category
register=template.Library()

@register.inclusion_tag('refine_options.html',takes_context=True)
def show_refine_options(context):
    request = context['request']
    categories=Category.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
    rooms=Room.objects.all()
    features={'color':colors,'room':rooms,'size':sizes,'category':categories}
    return {'features':features,'request':request}