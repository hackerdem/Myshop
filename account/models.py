from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from datetime import datetime
class Profile(models.Model):
    username=models.EmailField(_('Email address'),max_length=64,blank=False)
    name=models.TextField(_('name'),max_length=64,blank=False)
    surname=models.TextField(_('Family name'),max_length=128,blank=False)
    created=models.DateTimeField(auto_now_add=True,db_index=True)
    modified=models.DateTimeField(auto_now_add=True)
    address_1=models.CharField(_('address'),max_length=128,blank=True)
    address_2=models.CharField(_("address cont'd"),max_length=128,blank=True)
    city=models.CharField(_("city"),max_length=64,blank=True)
    zip_code=models.CharField(_("zip code"),max_length=4,default="3123")
    phone=models.TextField()
    
    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.username

class UserActivation(models.Model):
    user=models.ForeignKey(User)
    access_token=models.CharField(max_length=100)
    expire_date=models.DateTimeField(default=datetime.now())