# Generated by Django 5.1 on 2024-11-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bake_id', models.IntegerField()),
                ('bake_name', models.CharField(max_length=100)),
                ('bake_desc', models.CharField(max_length=200)),
                ('bake_price', models.IntegerField()),
                ('bake_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
