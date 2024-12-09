from django.db import models

# Create your models here.

class Kitten(models.Model):
    kitten_id = models.IntegerField()
    kitten_name = models.CharField(max_length=100)
    kitten_desc = models.CharField(max_length=200)
    kitten_price = models.IntegerField()
    kitten_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.kitten_name)