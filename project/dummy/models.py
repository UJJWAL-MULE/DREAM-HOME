from django.db import models

# Create your models here.
class details(models.Model):
    name= models.CharField(max_length=100)
    series=models.CharField(max_length=100)
    age=models.IntegerField()
    birthyear=models.IntegerField()