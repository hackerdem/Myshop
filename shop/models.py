from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
"""
class User(AbstractUser):
    class Meta(object):
        unique_together = ('email',)"""
class Category(models.Model):
    name=models.CharField(max_length=200,primary_key=True,
                          db_index=True)
    slug=models.SlugField(max_length=200,
                          db_index=True,
                          unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'  
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_feature',args=[(self.__class__.__name__).lower(),self.slug])

class Size(models.Model):
    name=models.CharField(max_length=200,primary_key=True,
                          db_index=True)
    slug=models.SlugField(max_length=200,
                          db_index=True,
                          unique=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='size'
        verbose_name_plural='sizes'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_feature',args=[(self.__class__.__name__).lower(),self.slug])

class Room(models.Model):
    name=models.CharField(max_length=200,primary_key=True,
                          db_index=True)
    slug=models.SlugField(max_length=200,
                          db_index=True,
                          unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='room'
        verbose_name_plural='rooms'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_feature',args=[(self.__class__.__name__).lower(),self.slug])

class Color(models.Model):
    name=models.CharField(max_length=200,primary_key=True,
                          db_index=True)
    slug=models.SlugField(max_length=200,
                          db_index=True,
                          unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='color'
        verbose_name_plural='colors'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_feature',args=[(self.__class__.__name__).lower(),self.slug])


class Product(models.Model):
    category=models.ForeignKey(Category,blank=False,null=False,related_name='products')
    size=models.ForeignKey(Size,blank=False,null=False,related_name='products')
    color=models.ForeignKey(Color,blank=False,null=False,related_name='products')
    room=models.ForeignKey(Room,blank=False,null=False,related_name='products')
    name=models.CharField(blank=False,null=False,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    number_of_click=models.PositiveIntegerField(default=0)
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='products_liked',blank=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

def get_image_filename(instance,filename):
    return "hi"
"""class Image(models.Model):
    img_product_id=models.ForeignKey(Product,related_name="img_product_id",on_delete=models.CASCADE)
    slug=slugify(img_product_id.name)
    image=models.ImageField(upload_to='products/slug',
                            verbose_name='Image',)
    def __str__(self):
        return self.img_product_id"""

