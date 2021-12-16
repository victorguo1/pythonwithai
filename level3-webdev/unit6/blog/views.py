# blog/views.py
from django.views.generic import ListView, DetailView,CreateView # new
from django.views.generic.edit import UpdateView,DeleteView # new
from django.urls import reverse_lazy # new
from .models import Post # new

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"

class PostDetailView(DetailView): # new 
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):    
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
