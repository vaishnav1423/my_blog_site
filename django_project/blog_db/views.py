from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }  # To Pass variable as Context to Template
    return render(request,'blog_db/home.html',context)

def about(request):
    return render(request,'blog_db/about.html',{'title': "About"})