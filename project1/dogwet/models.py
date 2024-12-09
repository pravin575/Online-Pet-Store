from django.db import models

# Create your models here.

class Iteams(models.Model):
    iteams_id = models .IntegerField()
    iteams_name = models.CharField(max_length=100)
    iteams_desc = models.CharField(max_length=200)
    iteams_price = models.IntegerField()
    iteams_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return str(self.iteams_name)