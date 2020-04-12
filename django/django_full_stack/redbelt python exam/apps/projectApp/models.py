from django.db import models
import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be atleast 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be atleast 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!!!!!!!")
        if len(postData['password']) < 8:
            errors['password'] = "Password should be atleast 8 characters"
        if postData['password'] != postData['confirmation']:
            errors['password'] = "Password and confirmation do not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!!!!!!!")
        if len(postData['password']) < 8:
            errors['password'] = "Password field must be included"
        if len(postData['email']) < 1:
            errors['password'] = "Email field must be included"
        return errors

class ThoughtManager(models.Manager):
    def thought_validator(self, postData):
        errors = {}
        if len(postData['thought']) < 5:
            errors['thought'] = "Thought must be atleast 5 characters!!!!!!!"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Thought(models.Model):
    thought = models.TextField()
    users_that_like = models.ManyToManyField(User, related_name = "liked_thoughts")
    created_by = models.ForeignKey(User, related_name = "thoughts_uploaded")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ThoughtManager()
# Create your models here.
