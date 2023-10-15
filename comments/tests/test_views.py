from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Comment
from posts.models import Post


class CommentListAPITestCase(APITestCase):
    """
    Test case for the CommentList generic views including:
        - list
        - create
    """
    def setUp(self):
        """
        Setup the test object instances
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            owner=self.user,
            title='Test post',
            content='This is a test post'
            )

    def test_comment_list(self):
        Comment.objects.create(
            owner=self.user, post=self.post, content='comment 1'
            )
        Comment.objects.create(
            owner=self.user, post=self.post, content='comment 2'
            )

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/comments/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)

    def test_comment_creation(self):
        """
        Tests a comment can be successfully created with valid data.
        """
        self.client.login(
            username='testuser', password='testpassword'
            )

        data = {
            'post': self.post.id,
            'content': 'New Comment'
        }

        response = self.client.post('/comments/', data, format='json')

        self.assertEqual(response.status_code, 201)


class CommentDetailTests(APITestCase):
    """
    Tests for the CommentDetail generic view, including:
        - retrieve
        - update
        - destroy/ delete
    """
    def setUp(self):
        """
        Setup test data.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            owner=self.user,
            title='Test post',
            content='This is a test post'
            )

    def test_retrieval_of_comment_details(self):
        """
        Test the GET/ retrieval of a specific comment instance.
        """
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment'
            )

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(f'/comments/{comment.id}/')

        self.assertEqual(response.status_code, 200)

    def test_comment_updates(self):
        """
        Tests the PUT or update of a specific comment instance returns
        a success code.
        Checks the data is updated correctly.
        """
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test Comment'
            )

        self.client.login(username='testuser', password='testpassword')

        data = {
            'content': 'Test comment updates',
        }

        response = self.client.put(
            f'/comments/{comment.id}/', data, format='json'
            )

        comment.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.content, 'Test comment updates')

    def test_delete_comment_authentcated_user_comment_owner(self):
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test Comment'
            )

        self.client.login(username='testuser', password='testpassword')

        response = self.client.delete(f'/comments/{comment.id}/')

        self.assertEqual(response.status_code, 204)

    def test_delete_comment_authentcated_user_not_owner(self):
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test Comment'
            )
        not_owner = User.objects.create_user(
            username='notowner', password='testpassword'
            )
        self.client.login(username='notowner', password='testpassword')

        response = self.client.delete(f'/comments/{comment.id}/')

        self.assertEqual(response.status_code, 403)

    def test_delete_comment_unauthentcated_user(self):
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test Comment'
            )

        response = self.client.delete(f'/comments/{comment.id}/')

        self.assertEqual(response.status_code, 403)
