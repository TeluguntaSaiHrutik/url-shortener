from django.db import models

# Create your models here.

class urlDB(models.Model):
    url=models.CharField(max_length=1000)
    shortened=models.CharField(max_length=20,unique=True)

