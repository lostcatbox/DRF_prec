from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
app_name = 'myapp'

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
