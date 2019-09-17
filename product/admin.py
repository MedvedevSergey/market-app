from django.contrib import admin
from .models import Product, Category, Characteristic, CharacteristicType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'rating', 'price']
    filter_horizontal = ['characteristics']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'characteristic_type']


@admin.register(CharacteristicType)
class CharacteristicTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
