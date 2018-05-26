from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from shop.templatetags import cart_update_tags


@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
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
    
