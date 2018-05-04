from django.contrib import admin
from .models import Product,Room,Size,Color
from account.models import UserActivation

class SizeAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Size,SizeAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Color,ColorAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Room,RoomAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','id','room','size','color','number_of_click','price','stock',
                  'available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['room','size','color','price','stock','available','number_of_click']
    prepopulated_fileds={'slug':('name',)}
admin.site.register(Product,ProductAdmin)


    

class UserActivationAdmin(admin.ModelAdmin):
    list_display=['user','access_token']
    
admin.site.register(UserActivation,UserActivationAdmin)