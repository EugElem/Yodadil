# Generated by Django 2.2 on 2019-05-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0016_auto_20190516_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugshopnet',
            name='pathNet',
            field=models.CharField(default=1, max_length=127),
            preserve_default=False,
        ),
    ]