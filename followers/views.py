from rest_framework import generics, permissions, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from craft_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List and create followers when user is logged in.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all().order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'owner__username',
        'created_on',
        'followed__username',
    ]
    search_fields = [
        'owner__username'
    ]
    filterset_fields = [
        'owner',
        'followed__profile'
    ]

    def perform_create(self, serializer):
        if self.request.user == serializer.validated_data.get('followed'):
            raise serializers.ValidationError("You cannot follow your own profile.")
        
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Display follower details and delete if user is logged in
    and follower owner.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
