# Generated by Django 5.1 on 2024-11-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]
