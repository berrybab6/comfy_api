# Generated by Django 4.0.3 on 2022-05-08 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='favoriteproduct',
            table='favorite',
        ),
    ]
