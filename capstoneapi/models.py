# from .serializers import ProductSerializer
from django.db import models



# your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField()
    price = models.IntegerField()



    def __str__(self):
        return self.title