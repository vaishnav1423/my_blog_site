from django.urls import path
from . import views

urlpatterns=[
    path('blog_db',views.home,name='blog_db-home'),
    path('about/',views.about,name='blog_db-about')
]