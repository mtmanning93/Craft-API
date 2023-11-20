from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from posts.models import Post
from ..models import Like


class LikeModelTest(TestCase):
    """
    TestCase for the Like Modal.
    Checks object creation and unique constriants.
    """
    def setUp(self):
        """
        Set up test object instances.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.post = Post.objects.create(
            title='Test Post', owner=self.user
            )

    def test_like_creation(self):
        """
        Test the relationship of a post and user instance to a like
        when a Like object is created.
        """
        like = Like.objects.create(owner=self.user, post=self.post)
        self.assertEqual(like.owner, self.user)
        self.assertEqual(like.post, self.post)

    def test_unique_together(self):
        """
        Test the unique together constraints by attempting to
        duplicate a like. IntegrityError is raised.
        """
        Like.objects.create(owner=self.user, post=self.post)

        # Create duplicate like with the same user
        with self.assertRaises(IntegrityError):
            Like.objects.create(owner=self.user, post=self.post)

    def test_str_method(self):
        """
        Tests the string method returns the correct string.
        """
        like = Like.objects.create(owner=self.user, post=self.post)
        self.assertEqual(str(like), f'{self.user}, {self.post}')
