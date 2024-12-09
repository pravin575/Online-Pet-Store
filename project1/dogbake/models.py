from django.db import models

# Create your models here.

class Bake(models.Model):
    bake_id = models.IntegerField()
    bake_name = models.CharField(max_length=100)
    bake_desc = models.CharField(max_length=200)
    bake_price = models.IntegerField()
    bake_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.bake_name)