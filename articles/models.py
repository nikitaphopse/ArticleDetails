from django.db import models


# Create your models here.

class Article(models.Model):
    rfid = models.CharField(max_length=50, unique=True)
    article_name = models.CharField(max_length=50)
    article_num = models.IntegerField()
    storage_location = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
