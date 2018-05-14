from django.shortcuts import render,redirect
from .models import PurchaseItem
from .forms import PurchaseCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from account.views import user_login
from .tasks import purchase_created
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Purchase
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

@staff_member_required
def admin_purchase_pdf(request,purchase_id):
    order=get_object_or_404(Purchase,id=purchase_id)
    html=render('purchases/purchase/pdf.html',{'order':order})
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="order_{}.pdf"'.format(purchase.id)
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT+'css/pdf.css')])
    return response

@staff_member_required
def admin_purchase_detail(request,order_id):
    purchase=get_object_or_404(Purchase,id=order_id)
    return render(request,'admin/purchases/purchase/detail.html',{'order':purchase})
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
                print('form is valid')
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