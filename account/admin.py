from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=['username','first_name','surname','address_1','address_2','city','zip_code','phone']
    readonly_fields=['username','first_name','surname',]
admin.site.register(Profile,ProfileAdmin)






