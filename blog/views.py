from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'david kim',
#         'title': 'Blog Post 1',
#         'content': 'First post',
#         'date_posted': 'August 27, 2019'
#     }, 
#     {
#         'author': 'king dawei',
#         'title': 'Blog Post 2',
#         'content': 'Second post',
#         'date_posted': 'August 28, 2019'
#     }
# ]

def home(request):
    context = {
        #'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
