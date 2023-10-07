from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(
            companies, many=True
        )
        return Response(serializer.data)
