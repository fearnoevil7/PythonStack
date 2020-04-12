from django.db import models
import re


class Task(models.Model):
    description = models.TextField()
    isCompleted = models.BooleanField()


# class UserManager(models.Manager):
#     def validator(self, postData):
#         errors = {}
#         if len(postData['name']) < 2:
#             errors['name'] = "first name must be atleast two characters"
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = ("Invalid email address!!!!!!!")
#         if len(postData['password']) < 5:
#             errors['password'] = "password must be atleast 8 characters"
#             return errors

class User(models.Model):
    username = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    # objects = UserManager()
# Create your models here.
