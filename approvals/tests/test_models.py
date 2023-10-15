from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Approval


class ApprovalModelTestCase(TestCase):
    """
    Testcase for the Approval model, including:
        - __str__ method
    """
    def setUp(self):
        """
        Setup test object instances.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
        )

        self.user2 = User.objects.create_user(
            username='user2', password='password2'
        )

        self.approval = Approval.objects.create(
            owner=self.user1, profile=self.user2.profile
        )

    def test_create_approval(self):
        """
        Checks if the approval is creatd successfully, with
        correct data.
        """
        self.assertEqual(self.approval.owner, self.user1)
        self.assertEqual(self.approval.profile, self.user2.profile)

    def test_str_method(self):
        """
        Checks the __str__ method returns the correct string and format.
        """
        self.assertEqual(
            str(self.approval), f'{self.user1}, {self.user2.profile}'
            )
