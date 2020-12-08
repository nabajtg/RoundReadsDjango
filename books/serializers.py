from rest_framework import serializers
from .models import Book, WishList, Dates

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

        def __init__(self, *args, **kwargs):
            super(BookSerializer, self).__init__(*args, **kwargs)
            self.fields['image1'] = serializers.CharField(required=True)
            self.fields['image2'] = serializers.CharField(required=True)


class WishListSearializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('__all__')

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields = ('__all__')