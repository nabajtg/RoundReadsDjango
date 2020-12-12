from django.db import models
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    sale_price = models.IntegerField(null=True)
    borrow_price = models.IntegerField(null=True)
    availability = models.CharField(max_length=20)
    image1 = models.TextField()
    image2 = models.TextField()
    poster_name = models.CharField(max_length=255)
    poster_email = models.CharField(max_length=255)
    views = models.IntegerField()
    is_borrowed = models.CharField(max_length=5, default="No")
    is_sold = models.CharField(max_length=5, default="No")
    is_verified = models.BooleanField(default=False)

class WishList(models.Model):
    user_id = models.CharField(max_length=255, unique=True, primary_key=True)
    wishlist = models.JSONField(blank=True)

class Dates(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

class Request(models.Model):
    book_id = models.CharField(max_length=5)
    request_for = models.CharField(max_length=20)
    borrowing_offer = models.IntegerField(blank=True)
    buying_offer = models.IntegerField(blank=True)
    message = models.CharField(max_length=500)
    requester_name = models.CharField(max_length=255)
    requester_email = models.CharField(max_length=255)
    seller_contact = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, default="pending")
    response = models.CharField(max_length=500, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, auto_now=False)



