from rest_framework import serializers
from .models import Profile
from companies.models import Company
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    'is_owner' checks if the request user owns the profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio', 'job',
            'created_on', 'updated_on', 'image',
            'is_owner', 'employer', 'following_id',
        ]

    def to_representation(self, instance):
        """
        Convert profile employer field from company.pk into
        company.name and company.location in a readable string format.
        """
        data = super().to_representation(instance)
        employer_pk = data.get('employer')
        if employer_pk is not None:
            try:
                company = Company.objects.get(pk=employer_pk)
                data['employer'] = f"{company.name} - {company.location}"
            except Company.DoesNotExist:
                pass
        return data
