from django.db import models
from colorfield.fields import ColorField
import uuid

class Person(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)
    color = ColorField(default='#FF0000')

class Messages(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Colortrends(models.Model):
    name = models.CharField(max_length=200)
    color = ColorField(default='#FF0000')