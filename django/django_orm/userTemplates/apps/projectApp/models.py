from django.db import models

class User(models.Model):
    first = models.CharField(max_length=45)
    last = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()


# Create your models here.
