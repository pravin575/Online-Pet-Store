from django.db import models

# Create your models here.

class Item(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.item_name)