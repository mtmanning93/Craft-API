from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.contrib.auth.models import User
from ..models import Follower
from ..serializers import FollowerSerializer


class FollowerListViewTest(APITestCase):
    """
    Test case for the follow list and create view.
    """
    def setUp(self):
        """
        Set up test objects.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )

    def test_create_follower(self):
        """
        Creates a follower instance with user1 using the 'post'
        method and checks the correct follower instance is created.
        """
        self.client.force_authenticate(user=self.user1)

        data = {'followed': self.user2.id}
        response = self.client.post('/followers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.get().followed, self.user2)

    def test_list_followers(self):
        """
        Checks that when a follower created the response data returns the
        correct number of followers in the followerlist.
        """
        Follower.objects.create(owner=self.user1, followed=self.user2)
        Follower.objects.create(owner=self.user2, followed=self.user1)

        self.client.force_authenticate(user=self.user1)
        response = self.client.get('/followers/')

        total_follower_count = response.data['count']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(total_follower_count, 2)


class FollowerDetailViewTest(APITestCase):
    """
    Tests for the FollowDetail view incuding:
        - retrieval
        - deletion
    """
    def setUp(self):
        """
        Set up test object instances.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        self.follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
            )

    def test_retrieve_follower(self):
        """
        Test the GET or retrieval follower API endpoint.
        Checks the followed id matches that of the follower instance in
        setUp.
        """
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f'/followers/{self.follower.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['followed'], self.user2.id)

    def test_delete_follower_authenticated_user(self):
        """
        Tests the destroy instance functionality.
        Uses an authenticated user to delete a follower instance
        they own.
        """
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(f'/followers/{self.follower.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)

    def test_delete_follower_unauthenticated_user(self):
        """
        Test to check that an unauthenticated user cannot delete
        a follower instance they do not own.
        Also checks correct error message is displayed.
        """
        self.client.force_authenticate(user=self.user2)

        response = self.client.delete(f'/followers/{self.follower.id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Follower.objects.count(), 1)

        expected_message = {
            'detail': ErrorDetail(
                string='You do not have permission to perform this action.',
                code='permission_denied'
                )
            }
        self.assertEqual(response.data['detail'], expected_message['detail'])
