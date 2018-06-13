from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.decorators.http import require_POST
from shop.models import Product,Image
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from shop.templatetags import cart_update_tags
from django.http import JsonResponse
from django.template import RequestContext
import json

@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    product.image=Image.objects.filter(product=product).filter(main_image=True)
    print(product.image)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,
                 quantity=1,# fix this later this should be defined in the model as default instead of writing here
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')
    #return HttpResponse(status=204)

def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart=Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})       
    coupon_apply_form=CouponApplyForm()
    return render(request,'cart/detail.html',{'cart':cart,'coupon_apply_form':coupon_apply_form})

def cart_add_ajax(request):
    cart=Cart(request)
    product_id=request.POST.get('product_id',None)
    product=get_object_or_404(Product,id=product_id) 
    cart.add(product=product,
                 quantity=1,# fix this later this should be defined in the model as default instead of writing here
                 update_quantity=1)
    return redirect('cart:cart_detail')

def carttotal(request):
    cart=Cart(request)
    print(cart)
    return cart

def product_custom_filter(request):
    #request_csrf_token = request.POST.get('csrfmiddlewaretoken', '')
    request_getdata = request.POST.get('form', None) 
    context=RequestContext(request)
    
    context['filters']="{'blue':'on'}"
    for i in json.loads(request_getdata):
        if i['value']=='on':print(i['name'])
    #filtered_products=Product.objects.filter(product=product).filter(color='blue')
    print('filtered_products')   
    return HttpResponse('ok')