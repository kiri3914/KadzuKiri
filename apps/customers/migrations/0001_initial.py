# Generated by Django 5.0.2 on 2024-03-04 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('count_product', models.IntegerField(default=0, verbose_name='Количество')),
                ('cost_product', models.IntegerField(default=0, verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество товаров')),
                ('total_price', models.FloatField(verbose_name='Стоимость')),
                ('added_ad', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='customers.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cart', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='clients/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_client', to='customers.client'),
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('home', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('number_apt', models.CharField(max_length=5, verbose_name='Номер квартиры')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_adress', to='customers.client')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_favorites', to='customers.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_favorites', to='products.product')),
            ],
        ),
    ]
