from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Company


class CompanyModelTest(TestCase):
    """
    Tests for Company model, including:
        - __str__ method
    """
    def setUp(self):
        """
        Setup user and company instances for tests.
        """
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.company = Company.objects.create(
            name='Test Company',
            owner=self.user,
            location='Test Location',
            type='Test Type'
        )

    def test_create_company(self):
        """
        Simple test to check the model instance is created with the
        correct data.
        """
        self.assertEqual(self.company.name, 'Test Company')
        self.assertEqual(self.company.owner, self.user)
        self.assertEqual(self.company.location, 'Test Location')
        self.assertEqual(self.company.type, 'Test Type')

    def test_company_str_method(self):
        """
        Tests the __str__ method returns the correct string.
        """
        self.assertEqual(str(self.company), 'Test Company')

    def test_user_is_added_as_owner_when_creating_company(self):
        """
        Tests that when adding a company the user will automatically
        be added as the company owner.
        """
        self.client.login(
            username='testuser', password='testpassword'
            )

        response = self.client.post('/companies/', {
            'name': 'Testing Co',
            'location': 'Test Street',
            'type': 'Testers'
        })

        self.assertEqual(response.status_code, 201)

        company = Company.objects.get(name='Testing Co')
        self.assertEqual(company.owner, self.user)
