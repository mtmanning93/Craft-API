from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Follower
from ..serializers import FollowerSerializer


class FollowerSerializerTest(APITestCase):
    def setUp(self):
        """
        Set up the test user objects.
        """
        self.user1 = User.objects.create(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create(
            username='user2', password='password2'
            )

    def test_serializer_with_valid_data(self):
        """
        Check the the serializer works with valid data input.
        First check the instance is created successfully (201)
        Then checks the object created is a Follower model instance.
        Then checks serialized field data.
        """
        data = {
            'owner': self.user1.id,
            'followed': self.user2.id
        }

        self.client.force_authenticate(user=self.user1)

        response = self.client.post('/followers/', data, format='json')
        self.assertEqual(response.status_code, 201)

        follower = Follower.objects.get(
            owner=self.user1, followed=self.user2
            )
        self.assertIsInstance(follower, Follower)
        self.assertEqual(follower.owner, self.user1)
        self.assertEqual(follower.followed, self.user2)

    def test_duplicate_follow(self):
        """
        Test the create method with a duplicate instance,
        check corretc error message.
        """
        Follower.objects.create(owner=self.user1, followed=self.user2)

        # Same data as Follower instance above
        data = {
            'owner': self.user1.id,
            'followed': self.user2.id
        }

        self.client.force_authenticate(user=self.user1)

        response = self.client.post('/followers/', data, format='json')
        self.assertEqual(response.status_code, 400)

        expected_error = {'info': ['possible duplicate follow']}

        self.assertEqual((response.data['info']), expected_error['info'][0])
