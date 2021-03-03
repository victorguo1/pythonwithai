# blog/views.py
from django.views.generic import ListView, DetailView # new
from .models import Post # new

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"

class BlogDetailView(DetailView): # new 
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"


