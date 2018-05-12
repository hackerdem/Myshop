from celery import task
from django.core.mail import send_mail
from .models import Purchase

@task
def purchase_created(purchase_id):
    purchase=Purchase.objects.get(id=order_id)
    subject='Order number {}'.format(purchase.id)
    message='Dear {}, \n\nYou have successfully placed an order.\
            Your order id is {}.'.format(purchase.first_name,purchase.id)
    mail_sent=send_mail(subject,
                        message,
                        'erdemaus@myshop.com',
                        [purchase.email]
    ) 

    return mail_sent