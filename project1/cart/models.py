from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='shop',default='')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.username)