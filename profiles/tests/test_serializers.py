from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.contrib.auth.models import User
from profiles.models import Profile
from companies.models import Company
from profiles.serializers import ProfileSerializer


class ProfileSerializerTest(APITestCase):
    """
    Test case for the ProfileSerializer, and the
    to_representation method.
    """
    def setUp(self):
        """
        Set up test Use and Profile data.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.profile = self.user.profile
        self.client = APIClient()

    def test_profile_serializer_with_updated_data(self):
        """
        Checks the ProrfileSerializer serializes updated data in the profile.
        """
        new_name = 'Updated Name'
        new_bio = 'Updated Bio'
        new_job = 'Updated Job'

        data = {
            'name': new_name,
            'bio': new_bio,
            'job': new_job,
        }

        serializer = ProfileSerializer(
            instance=self.profile,
            data=data,
            context={'request': self.client},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

        # Retrieve the updated profile from the database
        updated_profile = Profile.objects.get(owner=self.user)
        # Add assertions to verify the updated data
        self.assertEqual(self.profile.owner.username, 'testuser')
        self.assertEqual(updated_profile.name, new_name)
        self.assertEqual(updated_profile.bio, new_bio)
        self.assertEqual(updated_profile.job, new_job)

    def test_to_representation_employer_conversion(self):
        """
        Checks the employer field to_representation method changes form
        company.pk to company.name and company.location string when Company
        instance is added as profile.employer.
        """
        company_owner = User.objects.create_user(
            username='companyowner',
            password='companyownerpass'
        )
        company = Company.objects.create(
            name='Test Company',
            owner=company_owner,
            location='Test Location'
        )

        self.profile.employer = company
        self.profile.save()

        profile_detail_url = f'/profiles/{self.profile.pk}/'
        response = self.client.get(profile_detail_url)

        self.assertEqual(response.status_code, 200)

        # Serialize the profile using the serializer with the request context
        serializer = ProfileSerializer(
            instance=self.profile, context={'request': response.wsgi_request}
        )
        serialized_data = serializer.data

        self.assertIn('employer', serialized_data)
        self.assertEqual(
            serialized_data['employer'],
            f"{company.name} - {company.location}"
        )

    def test_to_representation_employer_not_found(self):
        """
        Checks if the profile.employer has an invalid company,
        e.g. company deleted. That the user employer is represented as 'null'.
        """
        # Create a test company owner
        company_owner = User.objects.create_user(
            username='companyowner',
            password='companyownerpass'
        )
        company = Company.objects.create(
            name='Test Company',
            location='Test Location',
            owner=company_owner
            )
        profile = self.user.profile
        profile.employer = company
        profile.save()
        # Delete the company before serializer
        company.delete()

        profile_detail_url = f'/profiles/{profile.pk}/'
        # Make a GET request to the profile detail URL
        response = self.client.get(profile_detail_url)

        self.assertEqual(response.status_code, 200)

        # Serialize the profile using the serializer with the request context
        serializer = ProfileSerializer(
            instance=profile, context={'request': response.wsgi_request}
            )
        serialized_data = serializer.data

        self.assertIn('employer', serialized_data)
        self.assertEqual(serialized_data['employer'], 'null')
