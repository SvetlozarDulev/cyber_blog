from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class UsersTests(TestCase):
    def test_user_creating(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test1",
            email="testing@example.com",
            password="test123"
        )

        self.assertEqual(user.username, "test1")
        self.assertEqual(user.email, "testing@example.com")
        self.assertTrue(user.is_active)

    def test_superuser_creating(self):
        User = get_user_model()
        user_admin = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuper@example.com",
            password="super123"
        )

        self.assertEqual(user_admin.username, "testsuperuser")
        self.assertEqual(user_admin.email, "testsuper@example.com")
        self.assertTrue(user_admin.is_superuser)


class SignUpTest(TestCase):

    def test_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, 'registration/signup.html')


