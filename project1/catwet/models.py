from django.db import models

# Create your models here.

class Catwet(models.Model):
    catwet_id = models.IntegerField()
    catwet_name = models.CharField(max_length=100)
    catwet_desc = models.CharField(max_length=200)
    catwet_price = models.IntegerField()
    catwet_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.catwet_name)
