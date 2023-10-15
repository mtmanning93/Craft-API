from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Company
from ..serializers import CompanySerializer


class CompanySerializerAPITest(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.company = Company.objects.create(
            name='Test Company',
            location='Test Location',
            owner=self.user
        )

    def test_company_serializer(self):
        """
        Checks all fields expected are in the serialized data.
        """
        response = self.client.get(f'/companies/{self.company.id}/')

        self.assertEqual(response.status_code, 200)

        data = response.data

        fields = [
            'id', 'name', 'owner', 'location', 'type',
            'created_on', 'is_owner', 'employee_count'
            ]

        for field in fields:
            self.assertIn(field, data)

    def test_get_is_owner_method(self):
        """
        Checs the is_owner field value is set to True
        if the owner is viewing the company.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/companies/{self.company.id}/')
        company_data = response.data

        self.assertTrue(company_data['is_owner'], True)
