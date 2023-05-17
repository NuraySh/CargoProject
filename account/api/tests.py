import json

from django.forms.models import model_to_dict
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from account.api.serializers import RegistrationSerializer
from account.factories import CustomUserFactory
from account.models import CustomUser, PhonePrefix, Warehouse

class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("api/", include("account.api.urls")),
    ]
    def setUp(self):
        self.phone_prefix = PhonePrefix.objects.create(prefix_number="+99470")
        self.warehouse = Warehouse.objects.create(name="GN")

        self.data = {
            "email": "n@gmail.com",
            "password": "12345",
            "first_name": "Nuray",
            "last_name": "Shahvalaldi", #dont accept Azerbaijani letters
            "gender": "f",
            "phone_prefix": self.phone_prefix.pk,
            "phone": "5899298",
            "gov_id_prefix": "AA",
            "gov_id": "1234567",
            "pin_code": "5zxu4pw",
            "birth_date": "1995-08-20",
            "branch": self.warehouse.pk,
        }


    def test_create_account(self):
        url = reverse("auth_register")
        response = self.client.post(url, self.data, format = "json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, "n@gmail.com")


    def test_firstname_valid(self):
        self.data["first_name"] = "Murad"
        serializer = RegistrationSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_firstname_invalid(self):
        self.data["first_name"] = "Nura7"
        serializer = RegistrationSerializer(data=self.data)
        serializer.is_valid()
        print(serializer.errors)
        self.assertEqual(serializer.errors["first_name"][0],"First name should only include letters." )

    def test_lastname_valid(self):
        self.data["last_name"] = "Shahvaladli"
        serializer = RegistrationSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_lastname_invalid(self):
        self.data["last_name"] = "Shag@3bad"
        serializer = RegistrationSerializer(data=self.data)
        serializer.is_valid()
        print(serializer.errors)
        self.assertEqual(serializer.errors["last_name"][0],"Last name should only include letters.")

    # def test_phone_valid(self):
    #     self.data["phone"] = "1234567"
    #     serializer = RegistrationSerializer(data=self.data)
    #     self.assertTrue(serializer.is_valid())
    
    # def test_phone_invalid(self):
    #     self.data["phone"] = "12345678"
    #     serializer = RegistrationSerializer(data=self.data)
    #     serializer.is_valid()
    #     print(serializer.errors)
    #     self.assertEqual(serializer.errors["phone"][0],"Phone should be numbers and only 7 digits")