from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
    {'author': 'Vaishnav Kedar',
    'title' : 'First Blog',
    'content': 'This is my first blog',
    'date_posted': 'May 26, 2022'
    },
    {
        'author': 'Aboli Kedar',
        'title' : 'Linear Regression',
        'content': 'Supervised Learning Algorithm',
        'date_posted': 'May 06, 2022'
    }
]

def home(request):
    context={
        'posts':posts
    }  # To Pass variable as Context to Template
    return render(request,'blog_db/home.html',context)

def about(request):
    return render(request,'blog_db/about.html',{'title': "About"})