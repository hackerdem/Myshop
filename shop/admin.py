from django.contrib import admin
from .models import Category,Product
from account.models import UserActivation

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','id','number_of_click','price','stock',
                  'available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','stock','available','number_of_click']
    prepopulated_fileds={'slug':('name',)}
admin.site.register(Product,ProductAdmin)


    

class UserActivationAdmin(admin.ModelAdmin):
    list_display=['user','access_token']
    
admin.site.register(UserActivation,UserActivationAdmin)