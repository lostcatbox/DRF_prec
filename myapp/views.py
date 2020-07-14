from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

class PostPageNumberPagination(PageNumberPagination):
    page_size = 2

class UserListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        username=(self.kwargs['username'])
        qs = qs.filter(
            username=username
        )

        return qs


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination
    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = [SearchFilter]
    search_fields = ['title']

    @action(detail=False)
    def public_list(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['patch'],detail=True)
    def set_public(self,request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'], author=self.request.user)




post_list = PostViewSet.as_view({
    'get':'list',
    'post': 'create',
})

post_detail = PostViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# class PostListAPIView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.data, status=400)
#
# class PostDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=204)
#
#
#
# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == "GET":
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(serializer.data)
#
#     else:
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     if request.method == "POST":
#         serializer = PostSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     if request.method == "DELETE":
#         post.delete()
#         return Response(status=204)
#
#     else:
#         serializer = PostSerializer(post, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#
#
#
# # Create your views here.
#
#
#
#
#
#
#
#
#
#
