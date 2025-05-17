from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination

from rest_framework import permissions
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Follow, Group, Post, Comment
from .permissions import OwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ('get')


class FollowViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    http_method_names = ('get', 'post')
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
