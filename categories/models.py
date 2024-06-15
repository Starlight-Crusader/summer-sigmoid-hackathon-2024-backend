from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    parameters_list = ArrayField(
        models.CharField(max_length=40),
        blank=False,
        null=False,
    )
