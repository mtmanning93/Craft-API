from rest_framework.test import APITestCase, APIClient
from rest_framework import status, serializers
from django.contrib.auth.models import User
from ..models import Company


class CompanyListTests(APITestCase):
    """
    TestCase for the CompanyList view, including:
        - list
        - create
        - validate_company method
    """
    def setUp(self):
        """
        Set up the test objects and clients.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_valid_company_creation(self):
        """
        Tests the creation of a company is successful with valid data.
        """
        data = {
            'name': 'Test Company',
            'location': 'Test Location',
        }

        response = self.client.post('/companies/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_validate_company_with_valid_new_company_data(self):
        """
        Test that a new company passes validation with valid data
        """
        valid_new_data = {
            'name': 'New Company',
            'location': 'New Location'
            }
        response = self.client.post('/companies/', valid_new_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_validate_company_with_duplicate_company_name_and_location(self):
        """
        Checks for a '400_BAD_REQUEST' error if a user trys to create an exact
        duplicate company instance with a duplicate 'name' and 'location'
        field.
        """
        existing_company = Company.objects.create(
            name='Test Company', location='Test Location', owner=self.user
            )
        # Create a company with same 'name' and 'location' data
        duplicate_data = {
            'name': 'Test Company',
            'location': 'Test Location',
        }
        response = self.client.post(
            '/companies/', duplicate_data
            )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check the error message in the ValidationError
        self.assertEqual(
            str(response.data[0]),
            "A company with the title 'Test Company'"
            " and location 'Test Location' already exists."
        )

    def test_validate_max_amount_of_companies_per_user(self):
        """
        Checks the max limit of companies per user functionality.
        Creates 3 initial company instances with owner as the same user
        Then attempts to create a 4th company with same user as owner.
        """
        Company.objects.create(
            name='Company1', location='Location1', owner=self.user
            )
        Company.objects.create(
            name='Company2', location='Location2', owner=self.user
            )
        Company.objects.create(
            name='Company3', location='Location3', owner=self.user
            )
        company_4_data = {
            'name': 'New Company',
            'location': 'New Location'
            }

        response = self.client.post('/companies/', company_4_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            str(response.data[0]),
            "You have reached the max profile limit of 3 companies."
        )


class CompanyDetailTests(APITestCase):
    """
    TestCase for CompanyDetail view, include:
        - retrieve
        - update
        - destroy
    """
    def setUp(self):
        """
        Setup the user and company objects for testing.
        Setup the APIClient and login.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.company = Company.objects.create(
            name='Test Company', location='Test Location', owner=self.user
            )

        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_retrieval_of_specific_company(self):
        """
        Checks the GET or retrieval method of a specific comapny instance.
        """
        response = self.client.get(f'/companies/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company_details(self):
        """
        Checks the PUT request updates a companies information
        and the new details are stored correctly in db.
        """
        data = {
            'name': 'New Company Name',
            'location': 'New Location'
        }

        response = self.client.put(
            f'/companies/{self.company.id}/', data, format='json'
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'New Company Name')
        self.assertEqual(self.company.location, 'New Location')

    def test_delete_company_instance_authenticated_owner(self):
        """
        Checks the delete functionality for an authenticated user
        who owns the company instance.
        """
        response = self.client.delete(f'/companies/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_company_instance_authenticated_not_owner(self):
        """
        Checks the delete functionality for an authenticated user
        who does NOT own the company instance. Forbidden.
        """
        user2 = User.objects.create_user(
            username='newuser', password='testpassword'
            )
        self.client.login(
            username='newuser', password='testpassword'
            )
        response = self.client.delete(f'/companies/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
