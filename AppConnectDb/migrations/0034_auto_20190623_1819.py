# Generated by Django 2.2 on 2019-06-23 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0033_pattern'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pattern',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='class_price',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='price_re',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='price_tag',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='product_re',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='product_tag',
        ),
    ]
