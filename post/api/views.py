from rest_framework import pagination
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter
from post.api.paginations import PostPagination
from rest_framework.permissions import (
    IsAuthenticated,
)
from django.contrib.auth.models import User


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  # düzelecek burası
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
