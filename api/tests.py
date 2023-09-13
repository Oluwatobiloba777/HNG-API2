from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

# Create your tests here.


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {"name": "Mark Essein"}
        self.user = User.objects.create(**self.user_data)
        self.url = reverse("user_details", args=[self.user.pk])

    def test_create_user(self):
        url = reverse("user")
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        update_data = {"name": "Mark Essein Updated"}
        response = self.client.put(self.url, update_data, format="json")

    def test_delete_user(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
