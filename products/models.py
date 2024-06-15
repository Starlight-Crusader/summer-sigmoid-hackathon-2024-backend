from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)