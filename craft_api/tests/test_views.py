from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
    )


class CraftApiViewsTest(APITestCase):
    """
    Tests case for the main project views, including:
        - root_route
        - logout_route
    """
    def setUp(self):
        """
        Setup tests objects.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_root_route(self):
        """
        Test the root_route or 'landing page' returns successfully and with
        the correct welcome message.
        """
        response = self.client.get('')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "message":
                "Welcome to the craft-api for the Craft social media app."
            }
        )

    def test_logout_view_response(self):
        """
        Tests the logout view @api_view credentials are set and return
        correctly.
        Check response status code
        Check they are set to expire
        Check httponly attribute
        Check max_age is set to 0
        """
        response = self.client.post('/dj-rest-auth/logout/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.cookies[JWT_AUTH_COOKIE]['expires'],
            'Thu, 01 Jan 1970 00:00:00 GMT'
        )
        self.assertEqual(
            response.cookies[JWT_AUTH_REFRESH_COOKIE]['expires'],
            'Thu, 01 Jan 1970 00:00:00 GMT'
        )

        self.assertTrue(response.cookies[JWT_AUTH_COOKIE]['httponly'])
        self.assertTrue(response.cookies[JWT_AUTH_REFRESH_COOKIE]['httponly'])

        self.assertEqual(response.cookies[JWT_AUTH_COOKIE]['max-age'], 0)
        self.assertEqual(
            response.cookies[JWT_AUTH_REFRESH_COOKIE]['max-age'], 0
        )
