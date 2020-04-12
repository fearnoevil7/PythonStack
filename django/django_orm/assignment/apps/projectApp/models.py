from __future__ import unicode_literals
from django.db import models

class tvShowManager(models.Manager):
    def basic_validator(self, postData):
        print(postData)
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be atleast 3 characters"
        if len(postData['description']) < 10:
            errors['description'] = "Description should be atleast 10 characters"
        return errors

class tvShow(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    objects = tvShowManager()
# Create your models here.
