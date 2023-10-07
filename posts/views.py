from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request}
            )
        return Response(serializer.data)
