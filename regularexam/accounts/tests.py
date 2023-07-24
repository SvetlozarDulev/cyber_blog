from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersTests(TestCase):
    def test_user_creating(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test1",
            email="testing@example.com",
            password="test123"
        )

        self.assertEqual(user.username,"test1")
        self.assertEqual(user.email,"testing@example.com")
        self.assertTrue(user.is_active)
    def test_superuser_creating(self):
        User = get_user_model()
        user_admin = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuper@example.com",
            password="super123"
        )

        self.assertEqual(user_admin.username,"testsuperuser")
        self.assertEqual(user_admin.email,"testsuper@example.com")
        self.assertTrue(user_admin.is_staff)
        self.assertTrue(user_admin.is_superuser)
