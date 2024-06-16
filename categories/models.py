from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=50)
    parameters_list = ArrayField(
        models.CharField(max_length=40),
        blank=False,
        null=False,
    )
    icon_url = models.CharField(max_length=200, null=True)
