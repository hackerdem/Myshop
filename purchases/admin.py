from django.contrib import admin
from .models import Purchase,PurchaseItem
import csv
import datetime
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def order_pdf(obj):
    return '<a href="{}">PDF</a>'.format(reverse('purchases:admin_order_pdf',args=[obj.id]))
order_pdf.allow_tags=True
order_pdf.short_description='PDF Bill'
def purchase_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('purchases:admin_purchase_detail',args=[obj.id]))
purchase_detail.allow_tags=True

def export_to_csv(modeladmin,request,queryset):
    opts=modeladmin.model._meta
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename={}.csv'.format(opts.verbose_name)
    writer=csv.writer(response)
    fields=[field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row=[]
        for field in fields:
            value=getattr(obj,field.name)
            if isinstance(value,datetime.datetime):
                value=value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description='Export to CSV'
class PurchaseItemInline(admin.TabularInline):
    model=PurchaseItem
    raw_id_fields=['product']

class PurchaseAdmin(admin.ModelAdmin):
    list_display=['id','shipping_first_name','shipping_last_name','shipping_email',
    'shipping_address','shipping_postcode',
                    'shipping_city','paid','created','updated',purchase_detail,order_pdf]
    list_filter=['paid','created','updated']
    inlines=[PurchaseItemInline]
    actions=[export_to_csv]
admin.site.register(Purchase,PurchaseAdmin)
