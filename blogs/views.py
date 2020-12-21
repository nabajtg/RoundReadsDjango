from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class SetPagination(PageNumberPagination):
    page_size = 5

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-date_published')
    serializer_class = BlogSerializer
    pagination_class = SetPagination

class TrendingBlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-likes')[:3]
    serializer_class = BlogSerializer