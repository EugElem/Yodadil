# Generated by Django 2.2 on 2019-05-16 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0015_search_requestnumder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='requestNumder',
            new_name='requestNumber',
        ),
    ]