from django.contrib import admin
from .models import Purchase,PurchaseItem


class PurchaseItemInline(admin.TabularInline):
    model=PurchaseItem
    raw_id_fields=['product']

class PurchaseAdmin(admin.ModelAdmin):
    list_display=['id','shipping_first_name','shipping_last_name','shipping_email',
    'shipping_address','shipping_postcode',
                    'shipping_city','paid','created','updated']
    list_filter=['paid','created','updated']
    inlines=[PurchaseItemInline]
admin.site.register(Purchase,PurchaseAdmin)
