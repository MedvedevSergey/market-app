from django.db import models
from mptt.models import MPTTModel


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    characteristics = models.ManyToManyField('Characteristic', blank=True)
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена')
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name="Наименование категории")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children')

    def __str__(self):
        return self.title


class Characteristic(models.Model):
    title = models.CharField(max_length=255)
    characteristic_type = models.ForeignKey('CharacteristicType', on_delete=models.CASCADE,
                                            related_name='characteristics', )

    def __str__(self):
        return f'{self.title} {self.characteristic_type}'


class CharacteristicType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
