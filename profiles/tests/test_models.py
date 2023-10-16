from django.test import TestCase
from django.contrib.auth.models import User
from companies.models import Company
from ..models import Profile


class ProfileModelTests(TestCase):
    """
    Tests for the Profile model and create_profile method within.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )

    def test_profile_creation(self):
        """
        Checks if a profile is automatically created for the user instance when
        a User is created, and the dunder string method returns the
        correct string.
        """
        self.assertIsInstance(self.user.profile, Profile)
        self.assertEqual(self.user.profile.owner, self.user)
        self.assertEqual(str(self.user.profile), "testuser's profile")

    def test_profile_employer_relationship(self):
        """
        Checks the relationship between the company and employer field in the
        profile object.
        Also verifies the reverse relationship of the 'current_employee'
        from company to profile.
        """
        company_owner = User.objects.create_user(
            username='companyowner', password='companyownerpass'
            )
        company = Company.objects.create(
            name='Test Company', owner=company_owner, location='Test Location'
            )

        self.user.profile.employer = company
        self.user.profile.save()

        self.assertEqual(self.user.profile.employer, company)
        # Reverse relationship using 'current_employee'
        self.assertEqual(company.current_employee.first(), self.user.profile)
