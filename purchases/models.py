from django.db import models
from shop.models import Product

class Purchase(models.Model):
    shipping_first_name=models.CharField(max_length=50,blank=False,null=False)
    shipping_last_name=models.CharField(max_length=50,blank=False,null=False)
    shipping_email=models.EmailField(blank=False)
    shipping_address=models.CharField(max_length=250,blank=False,null=False)
    shipping_landmark=models.CharField(max_length=250)
    shipping_country=models.CharField(max_length=50,blank=False,null=False)
    shipping_state=models.CharField(max_length=50)
    shipping_city=models.CharField(max_length=50,blank=False,null=False)
    shipping_postcode=models.CharField(max_length=50,blank=False,null=False)
    #billing
    billing_first_name=models.CharField(max_length=50,blank=False,null=False)
    billing_last_name=models.CharField(max_length=50,blank=False,null=False)
    billing_email=models.EmailField(blank=False)
    billing_address=models.CharField(max_length=250,blank=False,null=False)
    billing_landmark=models.CharField(max_length=250)
    billing_country=models.CharField(max_length=50,blank=False,null=False)
    billing_state=models.CharField(max_length=50)
    billing_city=models.CharField(max_length=50,blank=False,null=False)
    billing_postcode=models.CharField(max_length=50,blank=False,null=False)
    use_shipping_for_billing=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)
    

    class Meta:
        ordering=('-created',)
    
    def __str__(self):
        return 'Purchase {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class PurchaseItem(models.Model):
    purchase=models.ForeignKey(Purchase,related_name='items')
    product=models.ForeignKey(Product,related_name='purchase_items')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity
