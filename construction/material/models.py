from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):

    name = models.CharField(max_length=20, verbose_name='Название категории: ')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name='Под категория: ')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Под категория'
        verbose_name_plural = 'Под категории'


class Product(models.Model):
    name = models.CharField(max_length=520, verbose_name='Название продукта')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена')
    star = models.IntegerField(verbose_name='Рейтинг', default=0)
    review = models.CharField(max_length=20, verbose_name='Обзор')
    manufacturer = models.CharField(
        max_length=20, verbose_name='Производитель')
    article = models.CharField(max_length=20, verbose_name='Артикул')
    image = models.ImageField(
        verbose_name='Фотка Информация о тренере ',
        upload_to='photoProduct/%Y/%m/%d/')
    descriptions = models.TextField(verbose_name='Описание')
    delivery = models.TextField(verbose_name='Доставка')
    video = models.FileField(
        verbose_name='Видео',
        upload_to='videoProduct/%Y/%m/%d')
    category = models.CharField(max_length=20, verbose_name='Катигории')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
