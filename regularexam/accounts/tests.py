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

    def setUp(self) -> None:
        self.username = "vasko1"
        self.email = "vasko23@gmail.com"
        self.years_experience = 23
        self.password = "ebasimaikata123"
    def test_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse("signup"), data=
                                    {
                                        "username": self.username,
                                        "email": self.email,
                                        "years_experience": self.years_experience,
                                        "password1": self.password,
                                        "password2": self.password,
                                    }
                                    )

        self.assertEqual(response.status_code, 302)

        user = get_user_model().objects.all()
        self.assertEqual(user.count(),1)
        # self.assertEqual(user.username, self.username)
        # self.assertEqual(user.email, self.email)
