from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Comment
from posts.models import Post


class CommentModelTest(TestCase):
    """
    Tests for Comment model, including:
        - __str__ method
    """
    def setUp(self):
        """
        Setup test object instances.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post',
            owner=self.user
        )

        self.comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='This is a test comment'
        )

    def test_comment_creation(self):
        """
        Checks correct data is added when created a modal instance.
        """
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.owner, self.user)
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.content, 'This is a test comment')

    def test_comment_str(self):
        """
        Checks the correct string is returned by the __str__ method.
        """
        self.assertEqual(str(self.comment), 'This is a test comment')

    def test_comment_ordering(self):
        """
        Checks the comments are ordered as expected from the newest to oldest
        '-created_on'
        """
        # Create extra comment to check order
        comment1 = self.comment
        comment2 = Comment.objects.create(
            owner=self.user, post=self.post, content='Comment 2'
            )

        ordered_comments = Comment.objects.all()

        self.assertEqual(ordered_comments[0], comment2)
        self.assertEqual(ordered_comments[1], comment1)
