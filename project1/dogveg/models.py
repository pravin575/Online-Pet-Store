from django.db import models

# Create your models here.

class Veg(models.Model):
    veg_id = models.IntegerField()
    veg_name = models.CharField(max_length=100)
    veg_desc = models.CharField(max_length=200)
    veg_price = models.IntegerField()
    veg_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.veg_name)