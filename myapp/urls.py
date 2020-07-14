from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,PostViewSet, UserListAPIView
from .views import post_list, post_detail

app_name = 'myapp'

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('post/fbv/', post_list),
    path('post/fbv/<int:pk>/', post_detail),
    path('',include(router.urls)),
    path('u/<slug:username>/', UserListAPIView.as_view()),

]
