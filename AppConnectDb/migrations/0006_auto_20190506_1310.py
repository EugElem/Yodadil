# Generated by Django 2.2 on 2019-05-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0005_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
