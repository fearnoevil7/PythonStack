from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "First name should be atleast 3 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username should be atleast 3 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be atleast 8 characters"
        if postData['password'] != postData['confirmation']:
            errors['password'] = "Password and confirmation do not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors['password'] = "Password field must be included"
        if len(postData['username']) < 3:
            errors['username'] = "Username field must be included"
        if len(postData['username']) < 1:
            errors['username'] = "Username field must be included"
        return errors

class ItemManager(models.Manager):
    def thought_validator(self, postData):
        errors = {}
        if len(postData['item']) < 3:
            errors['item'] = "Item must be atleast 3 characters!!!!!!!"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    item = models.CharField(max_length=255)
    users_that_like = models.ManyToManyField(User, related_name = "liked_items")
    added_by = models.ForeignKey(User, related_name = "items_uploaded")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
# Create your models here.
