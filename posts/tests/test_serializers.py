from rest_framework.test import APITestCase, APIClient
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.urls import reverse
from django.core.files import File
from django.contrib.auth.models import User
from ..models import Post
from ..serializers import PostSerializer
from likes.models import Like


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


class PostSerializerImageValidationTests(APITestCase):
    """
    Tests the image validation method in the PostSerializer.
    validate_image.
    """
    def setUp(self):
        """
        Set up test object instances
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )
        self.client.force_authenticate(user=self.user)

    def test_validate_image_valid(self):
        """
        Check whether a valid image can be uploaded.
        """
        image_file = open('posts/tests/test_images/test_valid.png', 'rb')

        post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'image': File(image_file),
        }

        serializer = PostSerializer(data=post_data)

        self.assertTrue(serializer.is_valid())

    def test_validate_image_invalid_size(self):
        """
        Checks the ValidationError is raised with the correct message,
        if the image uploaded is greater than 2mb, meaning the serializer
        is invalid.
        """
        image_file = open('posts/tests/test_images/too_large.jpg', 'rb')

        post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'image': File(image_file),
        }

        serializer = PostSerializer(data=post_data)

        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        self.assertEqual(
            context.exception.detail['image'][0], 'Image size larger than 2MB!'
            )

    def test_validate_image_too_wide(self):
        """
        Tests the validate_image method raises the correct ValidationError
        and message if the image width is larger than 4096px.
        """
        image_file = open('posts/tests/test_images/test_wide.png', 'rb')

        post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'image': File(image_file),
        }

        serializer = PostSerializer(data=post_data)

        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        self.assertEqual(
            context.exception.detail['image'][0],
            'Image width larger than 4096px!'
            )

    def test_validate_image_too_high(self):
        """
        Tests the validate_image method raises the correct ValidationError
        and message if the image height is larger than 4096px.
        """
        image_file = open('posts/tests/test_images/test_high.png', 'rb')

        post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'image': File(image_file),
        }

        serializer = PostSerializer(data=post_data)

        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        self.assertEqual(
            context.exception.detail['image'][0],
            'Image height larger than 4096px!'
            )
