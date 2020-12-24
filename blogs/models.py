from django.db import models
from rest_framework import serializers

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    date_published = models.DateTimeField(auto_now_add=True, auto_now=False)
    publisher_name = models.CharField(max_length=200)
    publisher_dept = models.CharField(max_length=200, blank=True)
    publisher_email = models.CharField(max_length=200)
    likes = models.IntegerField()
    cover_photo = models.TextField()

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Blog
        
        def __init__(self, *args, **kwargs):
            super(BlogSerializer, self).__init__(*args, **kwargs)
            self.fields['cover_photo'] = serializers.CharField(required=True)
