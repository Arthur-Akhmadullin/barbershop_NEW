from django.db import models
from django.shortcuts import reverse
from time import time

from ckeditor_uploader.fields import RichTextUploadingField

from .utils import gen_slug

class News(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    body = RichTextUploadingField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title) + "-" + str(int(time()))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']


class Record(models.Model):
    RECORD_TIME = (('10.00', '10.00'), ('11.00', '11.00'), ('12.00', '12.00'), ('13.00', '13.00'), ('15.00', '15.00'), ('16.00', '16.00'), ('17.00', '17.00'))

    name = models.CharField(max_length=35)
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now=False)
    time = models.CharField(max_length=5, choices=RECORD_TIME, default=RECORD_TIME[1][1])
    confirmed = models.BooleanField(default=False)


class Price(models.Model):
    service_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=0)