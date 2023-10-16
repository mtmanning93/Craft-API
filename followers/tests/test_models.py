from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from ..models import Follower


class FollowerModelTest(TestCase):
    """
    Testscase for the Follower Model.
    """

    def setUp(self):
        """
        Set up test user objects.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
        )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
        )

    def test_follower_object_with_valid_data_creation(self):
        """
        Tests the follower object it created successfully with
        the expected field data.
        """
        follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )

        self.assertIsInstance(follower, Follower)
        self.assertEqual(follower.owner, self.user1)
        self.assertEqual(follower.followed, self.user2)

    def test_unique_together_constraint(self):
        """
        Checks that the duplicate follower object cannot be created
        throwing an IntegrityErro if attempted.
        """
        follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )

        # Try to create the same follower instance
        with self.assertRaises(IntegrityError):
            Follower.objects.create(owner=self.user1, followed=self.user2)

    def test_follower_str_method(self):
        """
        Checks the model __str__ method returns the expected string format.
        """
        follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )
        self.assertEqual(str(follower), f'{self.user1} {self.user2}')
