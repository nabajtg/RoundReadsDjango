from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from books import views
from blogs.views import BlogViewSet, TrendingBlogViewSet

router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('wishlist', views.WishListViewSet, basename='wishlist')
router.register('get_wishlist', views.GetWishListViewSet, basename='getwishList')
router.register('get_user_books', views.CurrentUserBookViewSet, basename='user_books')
router.register('dates', views.DateViewSet, basename='dates')
router.register('requests', views.RequestViewSet, basename='requests')
router.register('blogs', BlogViewSet, basename='blogs')
router.register('trending_blogs', TrendingBlogViewSet, basename='trendsblogs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    url(r'^api/', include(router.urls)),
]
