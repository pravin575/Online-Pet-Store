# Generated by Django 5.1 on 2024-11-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iteams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteams_id', models.IntegerField()),
                ('iteams_name', models.CharField(max_length=100)),
                ('iteams_desc', models.CharField(max_length=200)),
                ('iteams_price', models.IntegerField()),
                ('iteams_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
