# Generated by Django 4.0.3 on 2022-03-07 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_title', models.CharField(max_length=255)),
                ('prod_description', models.CharField(blank=True, max_length=255, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('price_updated_at', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('length', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('width', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('prod_image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('brand', models.CharField(blank=True, max_length=150, null=True)),
                ('prod_category', models.PositiveSmallIntegerField(choices=[(1, 'womens'), (2, 'mens'), (3, 'kids')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSizeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
                ('item_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.itemsize')),
            ],
            options={
                'db_table': 'item_colors',
            },
        ),
        migrations.AddField(
            model_name='itemsize',
            name='colors',
            field=models.ManyToManyField(related_name='item_sizes', through='products.ItemSizeColor', to='products.color'),
        ),
        migrations.AddConstraint(
            model_name='itemsizecolor',
            constraint=models.UniqueConstraint(fields=('item_size', 'color'), name='unique_size_color'),
        ),
    ]
