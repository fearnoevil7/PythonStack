from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'first name should be atleast 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'last name should be atleast 2 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = 'passwords do not match'
        if len(postData['password']) < 8:
            errors['password'] = 'password should be atleast 8 characters'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
# Create your models here.
