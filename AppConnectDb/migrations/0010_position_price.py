# Generated by Django 2.2 on 2019-05-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0009_remove_position_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='price',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
