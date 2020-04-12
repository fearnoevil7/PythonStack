from django.db import models
import re
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be atleast 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be atleast 2 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "email invalid"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be atleast 8 characters!"
        if postData['password'] != postData['confirmation']:
            errors['password'] = "Password entered and confirmed password does not match!"
        return errors

class BookManager(models.Manager):
    def addValidator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Must include a title!!!!!!!"
        if len(postData['description']) < 5:
            errors['description'] = "Description must be atleast 5 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# user class attributes
# liked_books = a list of books a given user likes
# books_uploaded = a list of books uploaded by a given user

class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
# Create your models here.
