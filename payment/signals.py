from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from purchases.models import Purchase
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO

def payment_notification(sender,**kwargs):
    ipn_obj=sender
    if ipn_obj.payment_status==ST_PP_COMPLETED:
        purchase=get_object_or_404(Purchase,id=ipn_obj.invoice)
        purchase.paid=True
        purchase.save()
        subject='Artsshop - Invoice no : {}'.format(purchase.id)
        message='Plase, find attached the invoice for your recent purchase.'
        email=EmailMessage(subject,message,'admin@myshop',[purchase.email])
        html=render_to_string('purchases/purchase/pdf.html',{'purchase':purchase})
        out=BytesIO()
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT+'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
        email.attach('order_{}.pdf'.format(purchase.id),
                    out.getvalue(),
                    'application/pdf')
        email.send()
valid_ipn_received.connect(payment_notification)