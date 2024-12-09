from django.db import models

# Create your models here.

class Puppy(models.Model):
    puppy_id = models.IntegerField()
    puppy_name = models.CharField(max_length=100)
    puppy_desc = models.CharField(max_length=200)
    puppy_price = models.IntegerField()
    puppy_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.puppy_name)
