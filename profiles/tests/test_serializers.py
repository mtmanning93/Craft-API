from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from profiles.models import Profile
from companies.models import Company
from profiles.serializers import ProfileSerializer


class ProfileSerializerTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.profile = self.user.profile

    def test_profile_serializer_with_updated_data(self):
        # Update the profile data
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
            data=data, context={'request': self.client},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
        # else:
        #     self.fail(f'Serializer is not valid: {serializer.errors}')

        # Retrieve the updated profile from the database
        updated_profile = Profile.objects.get(owner=self.user)

        # Add assertions to verify the updated data
        self.assertEqual(self.profile.owner.username, 'testuser')

        self.assertEqual(updated_profile.name, new_name)
        self.assertEqual(updated_profile.bio, new_bio)
        self.assertEqual(updated_profile.job, new_job)
        # Add more assertions for other fields as needed

    def test_to_representation_employer_conversion(self):
        # Create a test company
        company_owner = User.objects.create_user(
            username='companyowner',
            password='companyownerpass'
        )
        company = Company.objects.create(
            name='Test Company',
            owner=company_owner,
            location='Test Location'
        )

        # Set the employer field to the company
        self.profile.employer = company
        self.profile.save()

        # Create a mock request for the serializer
        # Adjust the URL as needed
        request = APIRequestFactory().get('/dummy-url/')
        request.user = self.user

        # Serialize the profile using the serializer with the request context
        serializer = ProfileSerializer(
            instance=self.profile, context={'request': request}
        )

        # Ensure the serializer has correctly converted the employer field
        serialized_data = serializer.data
        self.assertIn('employer', serialized_data)
        self.assertEqual(
            serialized_data['employer'],
            f"{company.name} - {company.location}"
        )

    def test_to_representation_employer_not_found(self):
        # Create a test company owner
        company_owner = User.objects.create_user(
            username='companyowner',
            password='companyownerpass'
        )

        # Create a test profile
        profile = self.user.profile

        # Create a test company
        company = Company.objects.create(
            name='Test Company',
            location='Test Location',
            owner=company_owner
            )

        # Set the employer field to the company
        profile.employer = company
        profile.save()

        # Delete the company before serialization
        company.delete()

        # Create a mock request using APIRequestFactory
        # Adjust the URL as needed
        request = APIRequestFactory().get('/dummy-url/')
        request.user = self.user

        # Serialize the profile using the serializer with the request context
        serializer = ProfileSerializer(
            instance=profile, context={'request': request}
            )

        # Ensure the serializer correctly handles a missing company
        serialized_data = serializer.data
        self.assertIn('employer', serialized_data)
        self.assertEqual(serialized_data['employer'], None)
