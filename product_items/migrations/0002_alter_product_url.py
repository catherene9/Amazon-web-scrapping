# Generated by Django 3.2.6 on 2021-08-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=200, verbose_name='url'),
        ),
    ]
