from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from decimal import Decimal
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from purchases.models import Purchase
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    return render(request,'payment/done.html')

@csrf_exempt
def payment_cancelled(request):
    return render(request,'payment/canceled.html')

def payment_process(request):
    print('comes to payment')
    purchase_id=request.session.get('purchase_id')
    print(purchase_id)
    purchase=get_object_or_404(Purchase,id=purchase_id)
    host=request.get_host()

    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'amount':'%.2f' % purchase.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(purchase.id),
        'invoice':str(purchase_id),
        'currency_code':'USD',
        'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('payment:done')),
        'cancel_return':'http://{}{}'.format(host,reverse('payment:canceled')),
        }

    form=PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request,'payment/process.html',context)