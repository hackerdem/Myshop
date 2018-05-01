from django.shortcuts import render
from .models import PurchaseItem
from .forms import PurchaseCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required
def check_user_registration(request):
    if request.user.is_authenticated():
        form=PurchaseCreateForm
        return render(request,'purchases/purchase/shippinginfo.html',{'form':form})
    else:
        return render(request,'account/account/login.html')

def purchase_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=PurchaseCreateForm(request.POST)
        if form.is_valid():
            purchase=form.save()
            for item in cart:
                PurchaseItem.objects.create(purchase=purchase,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
            cart.clear()
            return render(request,'purchases/purchase/created.html',{'purchase':purchase})

        else:
            form=PurchaseCreateForm()
        return render(request,'purchases/purchase/create.html',{'cart':cart,'form':form})