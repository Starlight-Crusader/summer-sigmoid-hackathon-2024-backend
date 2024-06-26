from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image_url = models.CharField(max_length=200, null=True)
    tinder_image_url = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)