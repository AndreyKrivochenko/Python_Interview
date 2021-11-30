from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ManyToManyField(Category, related_name='category', verbose_name='Категории')
    name = models.CharField(max_length=128, verbose_name='Название товара')
    receipt_date = models.DateTimeField(verbose_name='Дата поступления', auto_now_add=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=16, verbose_name='Единица измерения')
    provider_name = models.CharField(max_length=128, verbose_name='Имя поставщика')

    def __str__(self):
        return self.name
