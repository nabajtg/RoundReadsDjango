from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class SetPagination(PageNumberPagination):
    page_size = 12


class BookViewSet(viewsets.ModelViewSet):
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

class CurrentUserBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['=poster_email']
    filter_backends = (filters.SearchFilter,)

class SimilarBooksViewSet(viewsets.ModelViewSet):
    #queryset = Book.objects.filter(category='engineering')[:5]
    serializer_class = BookSerializer
    #search_fields = ['=category']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        category = self.request.query_params.getlist('category')
        print(category)
        queryset = Book.objects.filter(category__in=category)[:6]
        return queryset



class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSearializer

class GetWishListViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    def get_queryset(self):
        print(self.request.query_params.getlist('wishlist[]'))
        
        wishlist = self.request.query_params.getlist('wishlist[]')

        queryset = Book.objects.filter(id__in=wishlist)
        return queryset

class DateViewSet(viewsets.ModelViewSet):
    serializer_class = DateSerializer
    queryset = Dates.objects.all()

class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.order_by('-time')
    search_fields = ['=book_id', '=requester_email']
    filter_backends = (filters.SearchFilter,)

