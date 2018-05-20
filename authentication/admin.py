from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserRegistrationForm
from django.contrib.auth.models import Group
from authentication.models import User
from django import forms

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserRegistrationForm
    list_display=('email','first_name','is_admin')
    list_filter=('is_admin',)
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personel info',{'fields':('first_name',)}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','first_name','password','password2')}
        ),
    )
    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)