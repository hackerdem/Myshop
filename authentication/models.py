from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.utils.translation import ugettext as _
class UserManager(BaseUserManager):
    def create_user(self,email,first_name,password=None):
        if not email:
            raise ValueError('User must have an email address')
        user=self.model(email=self.normalize_email(email),
                        first_name=first_name,
                        )
        #add a function to check password requirements###############
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,password):
        user=self.create_user(email,password=password,first_name=first_name)
        user.is_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email=models.EmailField(verbose_name='Email address',max_length=255,unique=True,)
    first_name=models.TextField(_('Firstname'),max_length=255,blank=False,null=False)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name']
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin