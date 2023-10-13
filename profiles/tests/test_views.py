from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.views import ProfileDetail
from profiles.serializers import ProfileSerializer


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
        # Authenticate the user by logging in
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        # Define the URL for the profile detail view
        url_name = 'profile-detail'
        url = reverse(url_name, args=[self.user.pk])
        # Send a GET request to retrieve the profile
        response = self.client.get(url)
        # Verify that the response status code is HTTP 200 OK
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
        # Data for the update
        updated_data = {
            'name': 'Updated Name',
            'job': 'Updated Job',
            'bio': 'Hi im updated, i work at updated.'
        }
        # Send a PUT request to update the profile
        response = self.client.put(url, updated_data, format='json')
        # Verify a successful update
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify that the profile data has been updated
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

    def test_unauthorized_user_cannot_update_profile_fields(self):
        """
        Checks that an unauthorized user cannot update a profile with new data:
            - job
            - bio
        """
        user_profile = self.user.profile
        # Create a request using the APIRequestFactory
        factory = APIRequestFactory()
        data = {'job': 'Updated Job', 'bio': 'Updated Bio'}
        request = factory.patch(reverse('profile-detail', args=[user_profile.pk]), data=data, format='json')
        # Create a different user (unauthorized user)
        unauthorized_user = User.objects.create_user(username="unauthorized", password="unauthorizedpass")
        # Authenticate the request with the unauthorized user
        request.user = unauthorized_user
        # Get the profile detail view
        view = ProfileDetail.as_view()
        # Perform a PATCH request to update job and bio fields
        response = view(request, pk=user_profile.pk)

        self.assertEqual(response.status_code, 403)  # Forbidden status code for unauthorized update
        user_profile.refresh_from_db()  # Ensure no changes were made to the profile
        self.assertEqual(user_profile.job, '')
        self.assertEqual(user_profile.bio, '')
