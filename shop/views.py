from django.shortcuts import render,get_object_or_404
from .models import Product,Size,Color,Room
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.cart import Cart
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def size_color_room_filter(request,slug):
    
    products=Product.objects.order_by('-{}'.format(slug))
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_list_by_feature(request,name,slug):
    cart=Cart(request)
    products=Product.objects.filter(**{slug:name.capitalize()}).order_by('-stock')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_list(request):
    cart=Cart(request)
    products=Product.objects.filter(available=True).order_by('-stock')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_most_viewed(request):
    products=Product.objects.filter(available=True).order_by('-number_of_click')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
# FEATURED willl be added urls and function
def product_latest(request):
    products=Product.objects.order_by('-created')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def collection_shop_list(request):
    products=Product.objects.filter(available=True).order_by('-stock')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/shop_list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def pagination(request,products):
    
    colors=Color.objects.all()
    sizes=Size.objects.all()
    rooms=Room.objects.all()
    paginator=Paginator(products,8)
    page=request.GET.get('page')
    features={'color':colors,'room':rooms,'size':sizes,}
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage: 
        products=paginator.page(paginator.num_pages)
    return products,paginator,features
    

    

def product_detail(request,id,slug):
    
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    product.number_of_click=product.number_of_click+1
    product.save()
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/product_detail.html',{'product':product,'cart_product_form':cart_product_form})
"""@require_POST   
def product_liked_by_user(request):
    product_id=request.POST.get('id')
    action=request.POST.get('action')
    if product_id and action:
        try:
            product=Product.objects.get(id=product_id)
            if action=='like':
                product."""
