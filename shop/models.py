from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
"""
class User(AbstractUser):
    class Meta(object):
        unique_together = ('email',)"""
class Product(models.Model):
    size=models.ForeignKey(Size,default=1,related_name='products')
    color=models.ForeignKey(Color,default=1,related_name='products')
    room=models.ForeignKey(Room,default=1,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    number_of_click=models.PositiveIntegerField(default=0)
    #like_number=models.PositiveIntegerField(default=0)
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])

def get_image_filename(instance,filename):
    return "hi"
"""class Image(models.Model):
    img_product_id=models.ForeignKey(Product,related_name="img_product_id",on_delete=models.CASCADE)
    slug=slugify(img_product_id.name)
    image=models.ImageField(upload_to='products/slug',
                            verbose_name='Image',)
    def __str__(self):
        return self.img_product_id"""

class Size(models.Model):
    name=models.CharField(max_length=200,
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
        return reverse('shop:product_list_by_size',args=[self.slug])

class Room(models.Model):
    name=models.CharField(max_length=200,
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
        return reverse('shop:product_list_by_room',args=[self.slug])

class Color(models.Model):
    name=models.CharField(max_length=200,
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
        return reverse('shop:product_list_by_color',args=[self.slug])