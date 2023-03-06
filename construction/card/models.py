from django.db import models
from material.models import Product


class Card(models.Model):
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    product = models.ForeignKey(Product, verbose_name='Корзина', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'



