from django.db import models

# Create your models here.
class Fest(models.Model):
    date = models.IntegerField()
    place = models.CharField(max_length=20)
    booth_num = models.IntegerField()
    name = models.CharField(max_length=50)
    sold_out = models.IntegerField()
    password = models.IntegerField()
    detail = models.TextField()
   
    def __str__(self):
        return self.name

