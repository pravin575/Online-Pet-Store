from django.db import models

# Create your models here.

class Premium(models.Model):
    premium_id = models.IntegerField()
    premium_name = models.CharField(max_length=100)
    premium_desc = models.CharField(max_length=200)
    premium_price = models.IntegerField()
    premium_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.premium_name)