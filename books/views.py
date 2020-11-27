from rest_framework import viewsets
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework import filters

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #search_fields = ['available_for', 'title', 'description', 'author']
    #filter_backends = (filters.SearchFilter,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

