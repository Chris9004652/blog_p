from django.urls import path
from . import views


app_name = 'blogg'


urlpatterns = [
    path('', views.home, name='home'), 
    path('article/<int:pk>/', views.article_detail, name='article_detail'), 
    path('search/', views.search_posts, name='search_posts'),
     path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]

