from django.shortcuts import render,redirect
from .models import PurchaseItem
from .forms import PurchaseCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from account.views import user_login
from .tasks import purchase_created
from django.core.urlresolvers import reverse
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
        print('request method post')
        form=PurchaseCreateForm(request.POST)
        try:
            if form.is_valid():
                print('for is valid')
                purchase=form.save()
                for item in cart:
                    PurchaseItem.objects.create(purchase=purchase,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                cart.clear()
                #launch asynchronous task
                purchase_created.delay(purchase.id)
                #set the order in the session
                request.session['purchase_id']=purchase.id
                #redirect to the payment
                return redirect(reverse('payment:process'))
        except Exception as e:
            print(e)
            form=PurchaseCreateForm()
        
        return render(request,'purchases/purchase/create.html',{'cart':cart,'form':form})