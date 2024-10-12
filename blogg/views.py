from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.shortcuts import  redirect  
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .utils import fetch_nyt_news 
import requests



def home(request):
    # Fetch NYT news
    api_key = 'jsufIIHfnWlwKTo0VGURAGUDmCYdu6kE'
    request_url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}"
    request_headers = {
        "Accept": "application/json"
    }

    response = requests.get(request_url, headers=request_headers)
    nyt_news = []

    if response.status_code == 200:
        articles = response.json().get('results', [])
        nyt_news = [
            {
                'title': article.get('title'),
                'url': article.get('url'),
                'abstract': article.get('abstract'),
                'image': article.get('multimedia')[0]['url'] if article.get('multimedia') else None
            }
            for article in articles
        ]
    
    # Fetch blog posts
    post = Post.objects.all()
    
    context = {
        'post': post,
        'nyt_news': nyt_news,
        'page_title': 'Welcome to West Side Blog'
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

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Handle files with request.FILES
        if form.is_valid():
            post = form.save(commit=False)  # Do not save to DB yet
            post.author = request.user      # Assign the logged-in user as the author
            post.save()                     # Save the post with the author set
            return redirect('blogg:home')     # Redirect to the post list
    else:
        form = PostForm()
    return render(request, 'blogg/add_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Ensure only the author can delete the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()
        return redirect('blogg:home')  # Redirect to post list after deletion

    return render(request, 'blogg/delete_post.html', {'post': post})