from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError


UserModel = get_user_model()

TEST_EMAIL = 'email@email.email'


class UserTestCase(TestCase):
    def test_username_not_required(self):
        user = UserModel.objects.create_user(
            email=TEST_EMAIL,
            password='Real Password',
        )

        self.assertTrue(user)

    def test_username_assigned_email(self):
        user = UserModel.objects.create_user(
            email=TEST_EMAIL,
            password='Real Password',
        )

        self.assertEqual(user.username, user.email)
        self.assertEqual(user.username, TEST_EMAIL)

    def test_normalize_email_1part(self):
        email = 'Name.Surname@domain.com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            email=email,
            password='Unreal Password #1',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_normalize_email_2part(self):
        email = 'name.surname@Domain.Com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            email=email,
            password='Unreal Password #2',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_normalize_email(self):
        email = 'Name.Surname@Domain.Com'
        normalized = 'name.surname@domain.com'

        user = UserModel.objects.create_user(
            email=email,
            password='Unreal Password #3',
        )

        self.assertEqual(user.email, normalized)
        self.assertNotEqual(user.email, email)

    def test_emails_unique_case_independent(self):
        email = 'jlennon@beatles.com'
        EMAIL = email.upper()
        UserModel.objects.create_user(
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
