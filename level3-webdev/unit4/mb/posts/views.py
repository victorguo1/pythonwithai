from django.views.generic import ListView # new
from .models import Post # new

class HomePageView(ListView): # new
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"

