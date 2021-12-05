#from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy #handle redirect
from .forms import PostForm 
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post #what model use in this view
    template_name = 'home.html' #render
    
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy('home')
