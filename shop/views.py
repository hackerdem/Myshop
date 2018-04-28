from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.cart import Cart

def product_list(request):
    cart=Cart(request)
    products=Product.objects.filter(available=True).order_by('-stock')
    return pagination(request,products)
def product_most_viewed(request):
    products=Product.objects.filter(available=True).order_by('-number_of_click')
    return pagination(request,products)
# FEATURED willl be added urls and function
def product_latest(request):
    products=Product.objects.order_by('-created')
    return pagination(request,products)
def pagination(request,products):
    paginator=Paginator(products,8)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage: 
        products=paginator.page(paginator.num_pages)
    return render(request,'shop/product/list.html',
                        {'products':products,'paginator':paginator})

    

def product_detail(request,id,slug):
    
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    product.number_of_click=product.number_of_click+1
    product.save()
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/product_detail.html',{'product':product,'cart_product_form':cart_product_form})
    