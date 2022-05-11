# Generated by Django 4.0.3 on 2022-05-08 17:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_favoriteproduct_table'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='favoriteproduct',
            index_together={('wished_item', 'user_id')},
        ),
    ]
