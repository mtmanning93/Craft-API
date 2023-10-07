from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serilaizers.ReadOnlyField(source='owner.username')
    is_owner = serilaizers.SerializerMethodField()
    profile_id = serilaizers.ReadOnlyField(source='owner.profile.id')
    profile_image = serilaizers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'content', 'created_on',
            'updated_on', 'image', 'is_owner', 'profile_id',
            'profile_image',
        ]
