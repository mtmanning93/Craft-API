from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Company
from ..serializers import CompanySerializer


class CompanySerializerTests(APITestCase):
    """
    Testcase for the CompanySerializer, including:
        - fields
        - get_is_owner method
        - employee_count field
    """
    def setUp(self):
        """
        Setup the testcase user and company objects.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.company = Company.objects.create(
            name='Test Company',
            location='Test Location',
            owner=self.user
        )

        self.employee = User.objects.create_user(
            username='employee',
            password='testpassword'
        )

    def test_company_serialized_fields(self):
        """
        Checks all fields expected are in the serialized data.
        """
        response = self.client.get(f'/companies/{self.company.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        fields = [
            'id', 'name', 'owner', 'location', 'type',
            'created_on', 'is_owner', 'employee_count'
            ]

        for field in fields:
            self.assertIn(field, data)

    def test_get_is_owner_method(self):
        """
        Checks the is_owner field value is set to True
        if the owner is viewing the company.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/companies/{self.company.id}/')
        company_data = response.data

        self.assertTrue(company_data['is_owner'], True)

    def test_employee_count_increments(self):
        """
        Checks that the employee_count field will increment
        when a user updates their profile.employer field to a
        company instance as their employer.
        Uses profile.employer field related_name='current_employee'.
        """
        self.assertEqual(self.company.current_employee.count(), 0)

        # Add employer instance to profile
        self.employee.profile.employer = self.company
        self.employee.profile.save()
        self.company.refresh_from_db()

        self.assertEqual(self.company.current_employee.count(), 1)

    def test_employee_count_decrement(self):
        """
        Checks that the employee_count field will decrement
        when a user updates their profile to remove the company instance
        as their employer.
        Uses profile.employer field related_name='current_employee'.
        """
        # Add employer instance
        self.employee.profile.employer = self.company
        self.employee.profile.save()
        self.company.refresh_from_db()
        self.assertEqual(self.company.current_employee.count(), 1)

        # Remove employer
        self.employee.profile.employer = None
        self.employee.profile.save()
        self.company.refresh_from_db()

        self.assertEqual(self.company.current_employee.count(), 0)
