from rest_framework import viewsets
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class SetPagination(PageNumberPagination):
    page_size = 12
    #page_size_query_param = 'page_size'
    #max_page_size = 1000


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = SetPagination
    search_fields = ['title', 'desc', 'author']
    filter_backends = (filters.SearchFilter,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

