from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError
from rest_framework import status, serializers
from django.contrib.auth.models import User
from ..models import Approval
from ..serializers import ApprovalSerializer


class ApprovalSerializerTests(APITestCase):
    """
    Testcase for the ApprovalSerializer, including:
        - get_approved_profile
        - to_representation
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

        self.approval = Approval.objects.create(
            profile=self.user1.profile, owner=self.user2
        )

    def test_get_approved_profile_mathod(self):
        """
        Checks the approved_profile method returns the correct information.
        """
        serializer = ApprovalSerializer(instance=self.approval)

        self.assertEqual(serializer.data['profile'], self.user1.username)

    def test_to_representation_method(self):
        """
        After serializing the approval instance, checks to see if the
        'approved_profile' field is converted to 'profile' and that 'profile' is
        serialized as the name instead of profile.id.
        """
        serializer = ApprovalSerializer(instance=self.approval)

        self.assertIn('profile', serializer.data)
        self.assertNotIn('approved_profile', serializer.data)
        self.assertEqual(serializer.data['profile'], self.user1.username)

    def test_create_duplicate_approval(self):
        """
        Checks that if a duplicate approval is created, a custom
        ValidationError is raised and the correct error message is displayed.
        """
        data = {
            'profile': self.user1.profile.id
            }
        # Serialize the same data twice
        serialized_data1 = ApprovalSerializer(data=data)
        serialized_data2 = ApprovalSerializer(data=data)

        self.assertTrue(serialized_data1.is_valid())
        self.assertTrue(serialized_data2.is_valid())

        approval1 = serialized_data1.save(owner=self.user1)

        self.assertIsInstance(approval1, Approval)

        # Attempt to save the same approval a second time
        with self.assertRaises(ValidationError) as context:
            serialized_data2.save(owner=self.user1)

        self.assertEqual(
            context.exception.detail, {'info': 'possible duplicate approval'}
        )
