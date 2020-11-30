from rest_framework import viewsets
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class SetPagination(PageNumberPagination):
    page_size = 12

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = SetPagination
    search_fields = ['title', 'desc', 'author']
    filter_backends = (filters.SearchFilter,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookSaleViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(condition='lightUsed')
    serializer_class = BookSerializer
    pagination_class = SetPagination
    search_fields = ['title', 'desc', 'author']
    filter_backends = (filters.SearchFilter,)

"""
class TestView(APIView):
    def get(self, request):
        test_data_var = request.query_params['testData']
        page_num_var = request.query_params['pageNum']
"""

class TestView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    pagination_class = SetPagination
    search_fields = ['title', 'desc', 'author']
    filter_backends = (filters.SearchFilter,)
    
    def get_queryset(self):
        print(self.request.query_params.getlist('availability[]'))
        print(self.request.query_params.getlist('condition[]'))
        print(self.request.query_params.getlist('category[]'))
        
        condition = self.request.query_params.getlist('condition[]')
        availability = self.request.query_params.getlist('availability[]')
        category = self.request.query_params.getlist('category[]')

        if len(condition) > 0 and len(availability) > 0 and len(category) > 0 :
            print("all three")
            queryset = Book.objects.filter(condition__in=condition, category__in=category, availability__in=availability)
        elif len(condition) > 0 and len(availability) > 0:
            print("con and ava")
            queryset = Book.objects.filter(condition__in=condition, availability__in=availability)
        elif len(condition) > 0 and len(category) > 0:
            print("con and cat")
            queryset = Book.objects.filter(condition__in=condition, availability__in=availability)
        elif len(availability) > 0 and len(category) > 0:
            print("ava and cat")
            queryset = Book.objects.filter(category__in=category, availability__in=availability)
        elif len(condition) > 0:
            print("con only")
            queryset = Book.objects.filter(condition__in=condition)
        elif len(availability) > 0:
            print("ava only")
            queryset = Book.objects.filter(availability__in=availability)
        elif len(category) > 0:
            print("cat only")
            queryset = Book.objects.filter(category__in=category)
        else:
            queryset = Book.objects.all()    

        return queryset