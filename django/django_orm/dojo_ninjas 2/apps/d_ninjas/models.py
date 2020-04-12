from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojos = models.ForeignKey(Dojo, related_name = "ninjas")
