from django.db import IntegrityError
from rest_framework import serializers
from .models import Approval


class ApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Approval model.
    owner field also included as read only, when Approval list returned.
    Create method ensure no duplicate approvals.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Approval
        fields = [
            'id', 'owner', 'profile', 'created_on'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'info': 'possible duplicate approval'
            })
