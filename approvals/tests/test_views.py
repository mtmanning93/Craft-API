from rest_framework.test import APITestCase
from rest_framework import status, serializers
from django.contrib.auth.models import User
from ..models import Approval
from ..serializers import ApprovalSerializer


class ApprovalListTests(APITestCase):
    """
    Testcase for the ApprovalList view, including:
        - list
        - create
    """
    def setUp(self):
        """
        Setup the user and approval instances for the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
        )

        self.user2 = User.objects.create_user(
            username='user2', password='password2'
        )

        self.user3 = User.objects.create_user(
            username='user3', password='password3'
        )

        self.approval = Approval.objects.create(
            profile=self.user1.profile, owner=self.user2
        )

        self.client.force_authenticate(user=self.user1)

    def test_create_approval(self):
        """
        Tests the approval is addeed to the database when using
        the POST method.
        """
        data = {'profile': self.user2.profile.id}
        response = self.client.post('/approvals/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Approval.objects.count(), 2)

    def test_approval_list(self):
        """
        Tests the approvals are added to the approval list when valid.
        """
        response = self.client.get('/approvals/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

        data = {
            'profile': self.user3.profile.id,
        }
        response = self.client.post('/approvals/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/approvals/')

        self.assertEqual(response.data['count'], 2)

    def test_create_approval_own_profile(self):
        """
        Checks if an error is raised when trying to approve own profile.
        Checks for correct error message.
        """
        self.client.force_authenticate(user=self.user2)

        data = {
            'profile': self.user2.profile.id
        }

        response = self.client.post('/approvals/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data[0], 'You cannot approve your own profile.'
            )


class ApprovalDetailTests(APITestCase):
    """
    Testcase for the ApprovalDetail view, including:
        - retrieval GET
        - destroy DELETE
    """
    def setUp(self):
        """
        Setup object instances for testing.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )

        self.user2 = User.objects.create_user(
            username='user2', password='password2'
        )

        self.approval = Approval.objects.create(
            profile=self.user2.profile, owner=self.user1
            )

        self.client.force_authenticate(user=self.user1)

    def test_retrieve_speific_approval(self):
        """
        Checks the retrieval of a specific approval instance by id.
        """
        response = self.client.get(f'/approvals/{self.approval.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_approval = ApprovalSerializer(instance=self.approval).data
        self.assertEqual(response.data, serialized_approval)

    def test_delete_approval_if_authenticated_user_is_owner(self):
        """
        Checks if a user who is the owner can delete their approval instance.
        """
        response = self.client.delete(f'/approvals/{self.approval.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Approval.objects.filter(id=self.approval.id).exists())

    def test_delete_approval_if_authenticated_user_is_not_owner(self):
        """
        Checks whether a user who is NOT the owner can delete an approval
        instance.
        """
        self.client.force_authenticate(user=self.user2)

        response = self.client.delete(f'/approvals/{self.approval.id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Approval.objects.filter(id=self.approval.id).exists())
