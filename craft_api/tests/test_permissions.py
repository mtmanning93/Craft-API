from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..permissions import IsOwnerOrReadOnly
from posts.models import Post


class IsOwnerOrReadOnlyTest(APITestCase):
    """
    Testcase for the IsOwnerOrReadOnly permission.
    """
    def setUp(self):
        """
        Setup test user and post objects.
        """
        self.user1 = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )

        self.user2 = User.objects.create_user(
            username='testuser2', password='testpassword2'
        )

        self.user1_object = Post.objects.create(
            owner=self.user1, title='Post1', content='A post be user1')

        self.user2_object = Post.objects.create(
            owner=self.user2, title='Post2', content='A post be user2')

    def test_post_owner_has_read_and_update_access(self):
        """
        Checks if the owner of a post has both read capabilties and the access
        via the permission to update the post.
        """
        self.client.force_authenticate(self.user1)

        response = self.client.get(f'/posts/{self.user1_object.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'title': 'Updated title'
        }

        response = self.client.put(
            f'/posts/{self.user1_object.pk}/', update_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_owner_user_has_only_read_access(self):
        """
        Checks that the user who doesnt own a post can read the details but
        cannot update this post.
        """
        self.client.force_authenticate(self.user2)
        response = self.client.get(f'/posts/{self.user1_object.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'title': 'Updated title attempt'
        }

        response = self.client.put(
            f'/posts/{self.user1_object.pk}/', update_data
            )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unregistered_user_can_read_post_not_update(self):
        """
        Checks that an unauthenticated user can still access the post
        to read its data.
        """
        response = self.client.get(f'/posts/{self.user1_object.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'name': 'Updated Object'
        }
        # Test cannot update
        response = self.client.put(
            f'/posts/{self.user1_object.pk}/', update_data
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
