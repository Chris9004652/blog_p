from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    post=Post.objects.all()
    context={
        'post': post,
        'page_title':'west side blog'
    }
    return render(request, 'blogg/home.html', context)

def article_detail(request, pk):
    current_article = get_object_or_404(Post, pk=pk)
    articles = Post.objects.all()  # To list all articles in the sidebar
    context = {
        'current_article': current_article,
        'articles': articles
    }
    return render(request, 'blogg/article_detail.html', context)

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.all()  # Initially get all posts

    if query:
        posts = Post.objects.filter(title__icontains=query) 

    context = {
        'query': query,
        'posts': posts,
        'page_title': 'Search Posts'
    }
    
    return render(request, 'blogg/search_posts.html', context)

def category_posts(request, category_name):
    # Get the category based on the category name from the URL
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category)

    return render(request, 'blogg/category_posts.html', {'posts': posts, 'category': category})

