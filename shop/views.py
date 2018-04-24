from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    path=request.path
    if request.path=='/shop/latest/':
        products=Product.objects.order_by('-created')
    elif path=='/shop/all/':
        products=Product.objects.filter(available=True).order_by('-stock')
    elif path=='/shop/most_viewed/':
        products=Product.objects.filter(available=True).order_by('-number_of_click')
    paginator=Paginator(products,8)
    page=request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        products=paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,'shop/product/list_ajax.html',{'products':products})
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    return render(request,'shop/product/list.html',
                        {'category':category,
                        'categories':categories,
                        'products':products})

    

def product_detail(request,id,slug):
    
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    product.number_of_click=product.number_of_click+1
    product.save()
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})
    