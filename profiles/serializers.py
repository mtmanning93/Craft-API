from rest_framework import serializers
from .models import Profile, Company


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    'is_owner' checks if the request user owns the profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio', 'job',
            'created_on', 'updated_on', 'image',
            'is_owner', 'employer',
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
