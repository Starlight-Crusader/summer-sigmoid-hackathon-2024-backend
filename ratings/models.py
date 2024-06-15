from django.db import models
from users.models import User
from django.contrib.postgres.fields import ArrayField
from products.models import Product


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    values = ArrayField(
        models.IntegerField(),
        blank=True,
        null=True
    )
    comment = models.CharField(max_length=250, blank=True)