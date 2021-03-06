# Generated by Django 2.0.5 on 2018-05-25 18:37

from django.conf import settings
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=shop.models.get_image_filename, verbose_name='image')),
                ('main_image', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('number_of_click', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete='CASCADE', related_name='products', to='shop.Category')),
                ('color', models.ForeignKey(on_delete='CASCADE', related_name='products', to='shop.Color')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'room',
                'verbose_name_plural': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wish_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('productid', models.ManyToManyField(related_name='productid', to='shop.Product')),
                ('userid', models.ManyToManyField(related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(on_delete='CASCADE', related_name='products', to='shop.Room'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete='CASCADE', related_name='products', to='shop.Size'),
        ),
        migrations.AddField(
            model_name='product',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='products_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=None, on_delete='CASCADE', related_name='product', to='shop.Product'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
