from django.contrib.humanize.templatetags.humanize import naturaltime
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
    approved_profile = serializers.SerializerMethodField()
    created_on = serializers.SerializerMethodField()

    def get_approved_profile(self, obj):
        return obj.profile.owner.username

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    class Meta:
        model = Approval
        fields = [
            'id', 'owner', 'profile', 'created_on', 'approved_profile',
        ]

    def to_representation(self, instance):
        """
        Convert approved profile id field from profile.pk into
        profile.username in a readable string format.
        """
        representation = super().to_representation(instance)
        representation['profile'] = representation.pop('approved_profile')
        return representation

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'info': 'possible duplicate approval'
            })
