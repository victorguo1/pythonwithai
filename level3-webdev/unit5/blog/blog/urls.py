# blog/urls.py
from django.urls import path
from .views import HomePageView,BlogDetailView   # new

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(),name='post_detail'), #new
    path('',HomePageView.as_view(),name = 'home'),
]
