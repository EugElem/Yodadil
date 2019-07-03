# Generated by Django 2.2 on 2019-06-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0029_auto_20190623_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='class_name',
            field=models.CharField(default=1, max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='class_price',
            field=models.CharField(default='q', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='price_re',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='price_tag',
            field=models.CharField(default='e', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='product_re',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='product_tag',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]