from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Like
from ..serializers import LikeSerializer
from posts.models import Post


class LikeListCreateViewTest(APITestCase):
    """
    Testcase to check the list and create generic views.
    """
    def setUp(self):
        """
        Set up test object instances.
        """
        self.user1 = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.user2 = User.objects.create_user(
            username='testuser2', password='testpassword2'
            )
        self.post = Post.objects.create(
            title='Test Post 1', owner=self.user1
            )
        self.client = APIClient()

    def test_like_post(self):
        """
        Check the authenticated user can create a like and the
        like is listed.
        """
        # Login user 1 and create like
        self.client.force_authenticate(user=self.user2)
        response = self.client.post(f'/likes/', {'post': self.post.id})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Login user 2 and create like
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(f'/likes/', {'post': self.post.id})

        response = self.client.get('/likes/')

        total_likes_count = response.data['count']

        self.assertEqual(total_likes_count, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LikeDetailTest(APITestCase):
    """
    Test case to test the LikeDetail view including:
        - retreive
        - destroy
    """
    def setUp(self):
        """
        Set up test object instances.
        """
        self.user1 = User.objects.create_user(
            username='testuser1', password='testpassword1'
            )
        self.user2 = User.objects.create_user(
            username='testuser2', password='testpassword2'
            )
        self.post = Post.objects.create(title='Test Post', owner=self.user1)
        self.like = Like.objects.create(owner=self.user2, post=self.post)
        self.client = APIClient()

    def test_retrieve_like_detail(self):
        """
        Tests ability to retrive a specific Like instance.
        """
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(f'/likes/{self.like.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.like.id)

    def test_delete_like_authenticated_user(self):
        """
        Test the authenticated users' ability to delete a like.
        """
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f'/likes/{self.like.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Like.objects.filter(id=self.like.id).exists())

    def test_delete_like_unauthorized_user(self):
        """
        Tests an unauthorized users ability to delete a like,
        should be forbidden unless the user owns the like instance.
        """
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(f'/likes/{self.like.id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Like.objects.filter(id=self.like.id).exists())
