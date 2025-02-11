# Generated by Django 5.1 on 2024-11-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puppy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puppy_id', models.IntegerField()),
                ('puppy_name', models.CharField(max_length=100)),
                ('puppy_desc', models.CharField(max_length=200)),
                ('puppy_price', models.IntegerField()),
                ('puppy_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
