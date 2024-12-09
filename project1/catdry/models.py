from django.db import models

# Create your models here.

class Catdry(models.Model):
    catdry_id = models.IntegerField()
    catdry_name = models.CharField(max_length=100)
    catdry_desc = models.CharField(max_length=200)
    catdry_price = models.IntegerField()
    catdry_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.catdry_name)