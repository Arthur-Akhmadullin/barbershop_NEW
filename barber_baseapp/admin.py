from django.contrib import admin

from .models import News, Record, Price


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'time', 'confirmed']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'price']