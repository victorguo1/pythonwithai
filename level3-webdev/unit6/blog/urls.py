# blog/urls.py
from django.urls import path
from .views import (
    HomePageView,
    PostDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView) # new

urlpatterns = [
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'), # new
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'), # new
    path('post/new/',BlogCreateView.as_view(), name='post_new'),# new
    path('post/<int:pk>/', PostDetailView.as_view(),name='post_detail'), #new
    path('',HomePageView.as_view(),name = 'home'),
]
