from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from ..models import Post
from ..serializers import PostSerializer


class PostListAPITest(TestCase):
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

        self.post_data = {
            'title': 'Test Post 2',
            'content': 'I love testing'}

    def test_list_posts(self):
        """
        Test PostList view simple returns a successful response.
        Test created Post instance appear in the list.
        """
        url = reverse('post-list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_post(self):
        """
        Tests that an authenticated user can create a post and add it to
        the post list.
        Checks for a successful status code and that the posts count
        has been incremented.
        """
        url = reverse('post-list')
        client = APIClient()
        # Authenticate the client with a user
        client.force_authenticate(user=self.user)
        response = client.post(url, self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
