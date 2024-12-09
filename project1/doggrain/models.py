from django.db import models

# Create your models here.

class Grain(models.Model):
    grain_id = models.IntegerField()
    grain_name = models.CharField(max_length=100)
    grain_desc = models.CharField(max_length=200)
    grain_price = models.IntegerField()
    grain_image = models.ImageField(upload_to='images',default='')


    def __str__(self):
        return str(self.grain_name)

