# Generated by Django 2.2 on 2019-06-16 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0019_position_net'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='requ',
        ),
    ]
