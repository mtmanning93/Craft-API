from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the Company model.
    'is_owner' checks if the request user owns the profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Company
        fields = [
            'id', 'name', 'owner', 'location', 'created_on',
            'is_owner',
        ]
