from django.contrib import admin
from . models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'created_date', 'is_active', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


