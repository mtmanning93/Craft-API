from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import Comment
from ..serializers import CommentSerializer
from posts.models import Post


class CommentSerializerTests(APITestCase):
    """
    Testscase for the CommentSerializer, including:
        - get_is_owner
        - get_created_on
    """
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            owner=self.user,
            title='Test post',
            content='This is a test post'
        )
        self.comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content="This is a test comment."
        )

    def test_comment_serializer_adds_valid_comment_to_list(self):
        """
        Checks that valid serialized comments are added to the
        comment list.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/comments/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

    def test_comment_serializer_valid_data(self):
        """
        Checks serializers allows comment creation with valid data.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'post': self.post.id,
            'content': 'This is a new comment.',
        }
        response = self.client.post('/comments/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_comment_serializer_invalid_data(self):
        """
        Checks serializers throws 400_BAD_REQUEST error if invalid
        data is sent.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'post': '',  # Required field
            'content': 'Invalid data',
        }
        response = self.client.post('/comments/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_comment_serializer_when_updating_comment_valid_data(self):
        """
        Tests a comment updates with valid serializer data.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'content': 'This comment has been updated.',
        }
        response = self.client.put(
            f'/comments/{self.comment.id}/', data, format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, data['content'])

    def test_get_is_owner_method(self):
        """
        Checks the is_owner field value is set to True
        if the owner is viewing the comment.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/comments/{self.comment.id}/')
        comment_data = response.data

        self.assertTrue(comment_data['is_owner'])

    def test_get_created_on_method(self):
        """
        Test the created_on field is serialized to the correct naturlatime
        format.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/comments/{self.comment.id}/')

        comment_created_on = response.data['created_on']

        expected_created_on = naturaltime(comment_created_on)
        self.assertEquals(comment_created_on, expected_created_on)
