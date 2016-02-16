from django.db import models
from shengxiangzhen.settings import *
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('jelly', 'Taiwan Jelly'),
        ('beans', 'Green Beens'),
        ('cookie', 'Cookie'),
        ('snack', 'Snack'),
        ('giftset','Gift Set'),
    )
   
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=255)
    productStock = models.IntegerField()
    productCategory = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='jelly')
    productImage = models.FileField(upload_to=MEDIA_ROOT)
    
    def __unicode__(self):
        return self.productName;