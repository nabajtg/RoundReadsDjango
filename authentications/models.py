from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, fname, mname, lname, phone, address, yearOfEnrollment, yearOfGraduation, dept, roll, hostel, wishlist, liked_blogs, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, mname=mname, lname=lname, phone=phone, address=address, yearOfEnrollment=yearOfEnrollment, yearOfGraduation=yearOfGraduation, dept=dept, roll=roll, hostel=hostel, wishlist=wishlist, liked_blogs=liked_blogs)

        user.set_password(password)
        user.save()

        return user

    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    yearOfEnrollment = models.CharField(max_length=4, blank=True)
    yearOfGraduation = models.CharField(max_length=4, blank=True)
    dept = models.CharField(max_length=255, blank=True)
    roll = models.CharField(max_length=10, blank=True)
    hostel = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    wishlist = models.JSONField(blank=True, default=dict)
    liked_blogs = models.JSONField(blank=True, default=dict)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'mname', 'lname', 'phone', 'address', 'yearOfEnrollment', 'yearOfGraduation', 'dept', 'roll', 'hostel', 'wishlist', 'liked_blogs']

    
    def __str__(self):
        return self.email
