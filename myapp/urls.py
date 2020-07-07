from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import PostListAPIView, PostDetailAPIView
app_name = 'myapp'

urlpatterns = [
    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
]
