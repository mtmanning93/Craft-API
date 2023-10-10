from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from craft_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all posts.
    Allows for the post creation within the 'post' method
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'like__created_at',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    filterset_fields = [
        # user feed
        'owner__followed__owner__profile',
        # user liked posts
        'like__owner__profile',
        # user posts
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List all post details.
    Allows editing of a post if user is the owner, as well as
    deletions.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
