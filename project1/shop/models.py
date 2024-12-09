from django.db import models
from dogdry.models import Item
# Create your models here.

class Product(models.Model):
    categories = (('Dry Food','Dry Food'),('Wet Food','Wet Food'),('Puppy Food','Puppy Food'),('Grain Food','Grain Food'),('Baked Food','Baked Food'),('Veg Dog Food','Veg Dog Food'),('Premium Food','Premium Food'),('Dry Cat Food','Dry Cat Food'),('Wet Cat Food','Wet Cat Food'),('Kitten Food','Kitten Food'))
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=250)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images',default='')
    product_category = models.CharField(max_length=50,choices=categories,default='')

    def __str__(self):
        return str(self.product_name)