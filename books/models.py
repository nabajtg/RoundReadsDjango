from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    price = models.IntegerField()
    availability = models.CharField(max_length=20)
    image1 = models.TextField()
    image2 = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=50)