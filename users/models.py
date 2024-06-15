from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)
