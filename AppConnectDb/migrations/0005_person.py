# Generated by Django 2.2 on 2019-05-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConnectDb', '0004_delete_connecttab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]