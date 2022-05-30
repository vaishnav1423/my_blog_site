from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm    #this module creates usercreation form  
from django.contrib import messages                       #sending messages accross sessions
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)     # request.POST will specifically happens when we click submit button on signup
        if form.is_valid():                     # is_valid will validate the form entries and return true if valid
            form.save()                         #This will actually create the user 
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created for user {username}!!')  #sends success message to next page
            return redirect('blog_db-home')     # redirect back to home page 
    else:
        form=UserCreationForm()                 #if form is empty and loaded for first time

    return render(request,'users/register.html',{'form':form})  #calling register.html template with form context
