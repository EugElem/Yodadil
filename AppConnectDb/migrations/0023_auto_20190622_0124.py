# Generated by Django 2.2 on 2019-06-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0022_position_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='product_tag',
        ),
        migrations.AddField(
            model_name='drugshopnet',
            name='product_tag',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
