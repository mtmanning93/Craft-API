from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Company
        fields = [
            'id', 'owner', 'location', 'created_on'
        ]
