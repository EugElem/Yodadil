# Generated by Django 2.2 on 2019-06-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0023_auto_20190622_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugshopnet',
            name='class_name',
            field=models.CharField(default=1, max_length=127),
            preserve_default=False,
        ),
    ]
