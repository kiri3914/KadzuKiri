# Generated by Django 5.0.2 on 2024-03-04 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена товара')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('date_expired', models.DateField()),
                ('base_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
