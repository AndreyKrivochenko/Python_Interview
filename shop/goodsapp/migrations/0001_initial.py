# Generated by Django 3.2.9 on 2021-11-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название товара')),
                ('receipt_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('unit', models.CharField(max_length=16, verbose_name='Единица измерения')),
                ('provider_name', models.CharField(max_length=128, verbose_name='Имя поставщика')),
            ],
        ),
    ]
