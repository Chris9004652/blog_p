from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') 
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    description = models.TextField(default='No description available')
    published_date = models.DateTimeField(auto_now_add=True) 
    updated_date = models.DateTimeField(auto_now=True) 
    status = models.BooleanField(default=True)
    
    # New ForeignKey linking to Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True)

    def __str__(self):
        return f"{self.title} was written by {self.author} with the following {self.content} on {self.published_date} day, with this {self.image} and {self.description} "



    

    