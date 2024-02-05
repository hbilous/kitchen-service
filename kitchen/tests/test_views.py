from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Cook

COOK_LIST_URL = reverse("kitchen:cook-list")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="Test12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        Cook.objects.create(
            username="test1",
            password="test123"
        )
        Cook.objects.create(
            username="test2",
            password="test123"
        )
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook-list.html")

    def test_create_cook(self):
        form_data = {
            "username": "test_acc",
            "password1": "Test12345",
            "password2": "Test12345",
            "first_name": "Ivan",
            "last_name": "Chimadan",
            "years_of_experience": 5
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
