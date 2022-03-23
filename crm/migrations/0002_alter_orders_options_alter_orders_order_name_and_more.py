# Generated by Django 4.0.3 on 2022-03-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Телефон'),
        ),
    ]
