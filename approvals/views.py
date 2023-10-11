from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from craft_api.permissions import IsOwnerOrReadOnly
from .models import Approval
from .serializers import ApprovalSerializer


class ApprovalList(generics.ListCreateAPIView):
    """
    List and create approvals when logged in.
    """
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Approval.objects.all().order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'owner__username',
        'profile',
        'created_on',
    ]
    search_fields = [
        'profile__owner__username',
    ]
    filterset_fields = [
        'profile__owner',
        'owner',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApprovalDetail(generics.RetrieveDestroyAPIView):
    """
    Get an approval's details and delete it if owner by user and logged in.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ApprovalSerializer
    queryset = Approval.objects.all()
