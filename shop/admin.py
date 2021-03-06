from django.contrib import admin
from .models import Product,Room,Image,Size,Color,Category
from account.models import UserActivation



class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
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
class ImageAdmin(admin.TabularInline):
    model=Image
    list_editable=['main_image']
    raw_id_fields=['product']
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','id','category','room','size','color','number_of_click','price','stock',
                  'available','created','updated',]
    list_filter=['available','created','updated']
    readonly_fields=['number_of_click','users_like','slug']
    list_editable=['room','size','color','price','stock','category','available',]
    prepopulated_fileds={'slug':('name',)}
    inlines=[ImageAdmin]
admin.site.register(Product,ProductAdmin)


    

class UserActivationAdmin(admin.ModelAdmin):
    list_display=['user','access_token']
    
admin.site.register(UserActivation,UserActivationAdmin)