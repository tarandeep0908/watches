# Generated by Django 2.2.2 on 2019-07-12 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staunishing', '0004_auto_20190712_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ASIN',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Best_Seller_Rank',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Package_Dimensions',
        ),
    ]
