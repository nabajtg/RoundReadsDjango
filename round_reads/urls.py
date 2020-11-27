from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from books import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    url(r'^api/', include(router.urls)),
]
