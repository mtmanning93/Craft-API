from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post


class PostModelTest(TestCase):
    """
    Testcase for the Post model.
    """
    def setUp(self):
        """
        Setup test model instances
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )
        self.post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='This is a test post'
            )

    def test_default_image_added(self):
        """
        Checks the default image is set when a post is created
        without an image.
        """
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.image, '../logo_nobg_aac6d9.png')

    def test_str_method(self):
        """
        Tests the string method returns the correct string.
        """
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(str(post), f'{post.id} {post.title}')
