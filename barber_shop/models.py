from django.db import models
from django.shortcuts import reverse
from time import time

from ckeditor_uploader.fields import RichTextUploadingField

from .utils import gen_slug


class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.category)
        super().save(*args, **kwargs)


class ProductGroup(models.Model):
    group = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.group

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.group)
        super().save(*args, **kwargs)


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=35)
    slug = models.SlugField(max_length=35, blank=True, unique=True)

    def __str__(self):
        return self.manufacturer

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.manufacturer)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 related_name='product_category'
                                 )
    group = models.ForeignKey('ProductGroup',
                              on_delete=models.PROTECT,
                              related_name='product_group'
                              )
    name = models.ForeignKey('Manufacturer',
                             on_delete=models.PROTECT,
                             related_name='product_name'
                             )
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    article = models.CharField(max_length=20, db_index=True)
    preview_image = models.ImageField(upload_to='shop_gallery/preview', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    available = models.BooleanField(default=True)
    short_description = models.TextField(blank=True)
    description = RichTextUploadingField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.manufacturer

    def get_absolute_url(self):
        return reverse('shop_detail_page', kwargs={'group_slug': self.group.slug, 'slug': self.slug})

    #def get_update_url(self):
    #return reverse('post_update_url', kwargs={'slug': self.slug})

    #def get_delete_url(self):
    #return reverse('post_delete_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.category) + "-" + gen_slug(self.name) + "-" + str(int(time()))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated']


class Image(models.Model):
    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='shop_gallery', blank=True)



