from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from ..models import Post
from ..serializers import PostSerializer


class PostListAPITest(APITestCase):
    """
    Tests for the PostList view,
    including listing and creating.
    """
    def setUp(self):
        """
        Set up test object instances
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

    def test_list_posts(self):
        """
        Test PostList view simple returns a successful response.
        Test created Post instance appear in the list.
        """
        url = reverse('post-list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
