from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer
from craft_api.permissions import IsOwnerOrReadOnly


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(
            companies, many=True, context={'request': request}
        )
        return Response(serializer.data)


class CompanyDetail(APIView):
    serializer_class = CompanySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            company = Company.objects.get(pk=pk)
            self.check_object_permissions(self.request, company)
            return company
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(
            company, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(
            company, data=request.data, context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
