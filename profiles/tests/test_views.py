from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Profile
from ..views import ProfileDetail
from ..serializers import ProfileSerializer


class ProfileListTest(APITestCase):
    """
    Tests the retrieval of the Profiles list
    """
    def test_list_profiles(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailTest(APITestCase):
    """
    Tests the retrieval of specific profile instances.
    """
    def setUp(self):
        """
        Set up test data.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )

    def test_retrieve_profiles(self):
        """
        Tests the retrieval of a single profile instance.
        """
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        url = reverse('profile-detail', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieval_of_specific_profile(self):
        """
        Checks response status code.
        Checks response data is correct when retrieving a specific profile.
        """
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        profile = Profile.objects.get(owner=self.user)
        url = reverse('profile-detail', args=[profile.pk])
        profile.job = "Crafter"
        profile.save()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['owner'], "testuser")
        self.assertEqual(response.data['job'], "Crafter")

    def test_profile_updates(self):
        """
        Tests if a profile can be updated successfully, and with new data:
            - name
            - job
            - bio
        """
        self.client.login(
            username=self.user.username, password='testpass')

        profile = Profile.objects.get(owner=self.user)
        url = reverse('profile-detail', args=[profile.pk])

        self.assertEqual(profile.name, '')
        self.assertEqual(profile.job, '')
        self.assertEqual(profile.bio, '')

        updated_data = {
            'name': 'Updated Name',
            'job': 'Updated Job',
            'bio': 'Hi im updated, i work at updated.'
        }

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')
        self.assertEqual(response.data['job'], 'Updated Job')
        self.assertEqual(
            response.data['bio'], 'Hi im updated, i work at updated.'
        )

    def test_profile_image_default_is_set(self):
        """
        Test to check if profile image is set to the default profile image
        on profile creation
        """
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )

        profile = Profile.objects.get(owner=self.user)
        url = reverse('profile-detail', args=[profile.pk])

        self.assertEqual(
            profile.image,
            '../user_defualt_icon_d7nivg.png'
        )
