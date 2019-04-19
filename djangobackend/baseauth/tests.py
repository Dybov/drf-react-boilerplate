from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError


UserModel = get_user_model()


class UserTestCase(TestCase):
    def test_normalize_email_1part(self):
        email = 'Name.Surname@domain.com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            username='username',
            email=email,
            password='Unreal Password #1',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_normalize_email_2part(self):
        email = 'name.surname@Domain.Com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            username='username',
            email=email,
            password='Unreal Password #2',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_normalize_email(self):
        email = 'Name.Surname@Domain.Com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            username='username',
            email=email,
            password='Unreal Password #3',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_emails_unique_case_independent(self):
        email = 'jlennon@beatles.com'
        EMAIL = email.upper()
        UserModel.objects.create_user(
            username='john',
            email=email,
            password='Unreal Password #4 from d1g1ts t00!',
        )

        self.assertRaises(
            IntegrityError,
            UserModel.objects.create_user,
            username='another',
            email=EMAIL,
            password='Unreal Password #5 from d1g1ts t00!',
        )
