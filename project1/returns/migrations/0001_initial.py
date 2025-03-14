# Generated by Django 5.1.3 on 2025-03-03 11:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='returns.order')),
            ],
        ),
    ]
