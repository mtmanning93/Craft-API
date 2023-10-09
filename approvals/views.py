from rest_framework import generics, permissions
from craft_api.permissions import IsOwnerOrReadOnly
from .models import Approval
from .serializers import ApprovalSerializer


class ApprovalList(generics.ListCreateAPIView):
    """
    List and create approvals when logged in.
    """
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Approval.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApprovalDetail(generics.RetrieveDestroyAPIView):
    """
    Get an approval's details and delete it if owner by user and logged in.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ApprovalSerializer
    queryset = Approval.objects.all()
