# blog/views.py
from django.views.generic import ListView, DetailView,CreateView  
from django.contrib.auth.mixins import (
    LoginRequiredMixin, # new
    UserPassesTestMixin) # new
from django.views.generic.edit import UpdateView,DeleteView  
from django.urls import reverse_lazy  
from .models import Post  

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"

class BlogDetailView(DetailView):  
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','body']  # new

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, # new
                    UserPassesTestMixin, # new
                    UpdateView):    
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, # new
                    UserPassesTestMixin, # new
                    DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user