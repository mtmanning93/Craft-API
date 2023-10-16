from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Profile
from ..serializers import ProfileSerializer
from companies.models import Company


class ProfileSerializerTest(TestCase):
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
        data = {
            'name': 'Updated name',
            'bio': 'Updated bio',
            'job': 'Updated job',
        }

        serializer = ProfileSerializer(
            instance=self.profile,
            data=data,
            context={'request': self.client},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

        updated_profile = Profile.objects.get(owner=self.user)

        self.assertEqual(self.profile.owner.username, 'testuser')
        self.assertEqual(updated_profile.name, 'Updated name')
        self.assertEqual(updated_profile.bio, 'Updated bio')
        self.assertEqual(updated_profile.job, 'Updated job')

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

        response = self.client.get(f'/profiles/{self.profile.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

        response = self.client.get(f'/profiles/{profile.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the profile using the serializer with the request context
        serializer = ProfileSerializer(
            instance=profile, context={'request': response.wsgi_request}
            )
        serialized_data = serializer.data

        self.assertIn('employer', serialized_data)
        self.assertEqual(serialized_data['employer'], 'null')
