# accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    # /accounts/singup
    path('signup/',SignUpView.as_view(),name='signup'),
]
