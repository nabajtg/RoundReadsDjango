from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from books import views
from blogs.views import BlogViewSet, TrendingBlogViewSet, UserBlogViewSet

from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('wishlist', views.WishListViewSet, basename='wishlist')
router.register('get_wishlist', views.GetWishListViewSet, basename='getwishList')
router.register('get_user_books', views.CurrentUserBookViewSet, basename='user_books')
router.register('similar_books', views.SimilarBooksViewSet, basename='similar')
router.register('dates', views.DateViewSet, basename='dates')
router.register('requests', views.RequestViewSet, basename='requests')
router.register('blogs', BlogViewSet, basename='blogs')
router.register('trending_blogs', TrendingBlogViewSet, basename='trendsblogs')
router.register('user_blogs', UserBlogViewSet, basename='userblogs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    url(r'^api/', include(router.urls)),
    path('activate/<uid>/<token>/', RedirectView.as_view(url='http://localhost:3000/activate/%(uid)s/%(token)s/')),
    path('password/reset/confirm/<uid>/<token>/', RedirectView.as_view(url='http://localhost:3000/password/reset/confirm/%(uid)s/%(token)s/'))
]
