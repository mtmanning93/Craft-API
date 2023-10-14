from rest_framework.test import APITestCase, APIClient
from rest_framework import status, serializers
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from ..models import Post
from ..serializers import PostSerializer
from likes.models import Like

from rest_framework.exceptions import ValidationError


class PostSerializerTests(APITestCase):
    """
    TestCase for the Post serializer.
    Including the validate_image method, get_is_owner and get_like_id.
    """
    def setUp(self):
        """
        Set up test data
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )
        self.post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='This is a test post'
        )
        self.serializer = PostSerializer()

    def test_post_owner_field_when_user_owns_post(self):
        """
        Checks the post.owner field is serialized correctly to owner.username.
        Creates user, creates a post with user as the owner, then uses the
        serializer to check the value of the 'owner' field in the response
        data.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)

        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertIn('owner', data)
        self.assertEqual(data['owner'], 'testuser')

    def test_post_serializer_is_owner_field(self):
        """
        Checks the is_owner field is serialized to True if the current
        logged in user also owns the post. First Checking the successful
        response and then the is_owner field.
        """
        self.client.force_authenticate(user=self.user)

        url = reverse('post-detail', kwargs={'pk': self.post.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertIn('is_owner', data)
        self.assertTrue(data['is_owner'])

    def test_post_serializer_like_id_field(self):
        """
        Checks the like_id field returns the Like objects id, if
        the current logged in user has liked the post object instance.
        """
        self.client.force_authenticate(user=self.user)

        like = Like.objects.create(owner=self.user, post=self.post)
        url = reverse('post-detail', kwargs={'pk': self.post.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertIn('like_id', data)
        self.assertEqual(data['like_id'], like.id)

    def test_post_serializer_like_id_field_no_like(self):
        """
        Tests if the like_id field is serialized to 'None' if there is
        no like associated with the post from the currently logged in user.
        """
        self.client.force_authenticate(user=self.user)

        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertIn('like_id', data)
        self.assertIsNone(data['like_id'])

    def test_post_serializer_like_id_field_unauthenticated(self):
        """
        Checks that the like_id field is serialized to 'None' if the user is
        not authenticated.
        """
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        data = response.data

        self.assertIn('like_id', data)
        self.assertIsNone(data['like_id'])
