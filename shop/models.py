from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
class Category(models.Model):
    name=models.CharField(max_length=200,
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
        return reverse('shop:product_list_by_category',args=[self.slug])
class Product(models.Model):
    #category=models.ForeignKey(Category,related_name='products')
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
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])

def get_image_filename(instance,filename):
    image_title=instance.products.name
    slug=slugify(image_title)
    return "products/{}-/{}".format(slug,filename)
class Image(models.Model):
    img_product_id=models.ForeignKey(Product,related_name="img_product_id",on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_image_filename,
                            verbose_name='Image',)
    def __str__(self):
        return self.img_product_id
