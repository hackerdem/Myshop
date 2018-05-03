from django.shortcuts import render
from .models import PurchaseItem
from .forms import PurchaseCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from account.views import user_login

def check_user_registration(request):
    if request.user.is_authenticated():
        form=PurchaseCreateForm
        return render(request,'purchases/purchase/shippinginfo.html',{'form':form})
    else:
        print('aaaaa')
        return user_login(request)

def purchase_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=PurchaseCreateForm(request.POST)
        try:
            if form.is_valid():
                purchase=form.save()
                for item in cart:
                    PurchaseItem.objects.create(purchase=purchase,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                cart.clear()
                return render(request,'purchases/purchase/payment.html',{'purchase':purchase})
        except Exception as e:
            print(e)
            form=PurchaseCreateForm()
        
        return render(request,'purchases/purchase/create.html',{'cart':cart,'form':form})