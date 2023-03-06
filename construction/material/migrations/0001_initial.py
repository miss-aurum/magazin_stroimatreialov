# Generated by Django 4.1.6 on 2023-02-27 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название категории: ')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=520, verbose_name='Название продукта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('star', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('review', models.CharField(max_length=20, verbose_name='Обзор')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Производитель')),
                ('article', models.CharField(max_length=20, verbose_name='Артикул')),
                ('image', models.ImageField(upload_to='photoProduct/%Y/%m/%d/', verbose_name='Фотка Информация о тренере ')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('delivery', models.TextField(verbose_name='Доставка')),
                ('video', models.FileField(upload_to='videoProduct/%Y/%m/%d', verbose_name='Видео')),
                ('category', models.CharField(max_length=20, verbose_name='Катигории')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Под категория: ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Под категория',
                'verbose_name_plural': 'Под категории',
            },
        ),
    ]
