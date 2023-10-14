from django.db import IntegrityError
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from likes.models import Like
from likes.serializers import LikeSerializer
from posts.models import Post


class LikeSerializerTest(APITestCase):
    """
    Testcase for the LikeSerializer and create no-duplicate method.
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
        Teststhat the LikeSerializer can correctly create a
        like with valid data.
        Checks the created like is associated with the correct post.
        """
        data = {'post': self.post.id}
        serializer = LikeSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        like = serializer.save(owner=self.user)

        self.assertIsInstance(like, Like)
        self.assertEqual(like.post, self.post)

    def test_create_duplicate_like(self):
        """
        Checks that if a duplicate like is created an IntegrityError
        is raised.
        """
        data = {'post': self.post.id}
        serialized_data1 = LikeSerializer(data=data)
        serialized_data2 = LikeSerializer(data=data)
        self.assertTrue(serialized_data1.is_valid())
        self.assertTrue(serialized_data2.is_valid())

        like1 = serialized_data1.save(owner=self.user)

        self.assertIsInstance(like1, Like)
        self.assertRaises(IntegrityError)
