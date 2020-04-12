from django.core.exceptions import ValidationError
from django.db import models

def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
        '{} must be longer than 2'.format(value)
        )
def AtleastEight(value):
    if len(value) < 3:
        raise ValidationError(
        '{} must be longer than 8'.format(value)
        )
class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    email = models.EmailField()
    password = models.CharField(max_length=45, validators = [AtleastEight])
    confirmation = models.CharField(max_length=45, validators = [AtleastEight])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
