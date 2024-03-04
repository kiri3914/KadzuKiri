# Generated by Django 5.0.2 on 2024-03-04 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDeliver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('delivery_date', models.DateTimeField()),
                ('tracking_number', models.IntegerField()),
                ('delivery_cost', models.IntegerField()),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.adress')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.cart')),
                ('delivery_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.statusdeliver')),
            ],
        ),
    ]
