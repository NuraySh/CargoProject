import json

from django.forms.models import model_to_dict
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from account.api.serializers import RegistrationSerializer
from account.factories import CustomUserFactory
from account.models import CustomUser, PhonePrefix, Warehouse

# class AccountTests(APITestCase, URLPatternsTestCase):
#     urlpatterns = [
#         path("api/", include("account.api.urls")),
#     ]
# def setUp(self):
#     self.phone_prefix = PhonePrefix.objects.create(prefix_number="+99470")
#     self.warehouse = Warehouse.objects.create(name="GN")

#     self.data = {
#         "email": "n@gmail.com",
#         "password": "12345",
#         "first_name": "Nuray",
#         "last_name": "Şahvələdli",
#         "gender": "f",
#         "phone_prefix": self.phone_prefix.pk,
#         "phone": "5899298",
#         "gov_id_prefix": "AA",
#         "gov_id": "12345678",
#         "pin_code": "5zxu4pw",
#         "birth_date": "1995-08-20",
#         "branch": self.warehouse.pk,
#     }


# def test_create_account(self):

#     user = CustomUserFactory()
#     user_dict = model_to_dict(user)
#     print(user_dict)

#     url = reverse("auth_register")
#     response = self.client.post(url, user_dict, format = "json")
#     print(response.data)
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     # self.assertEqual(response.data, {"email": ["Email already exists."]})
#     # serializer = RegistrationSerializer(data=self.data)
#     # self.assertEqual(serializer.errors["gov_id"], "Please enter right numbers of digits(serializer)")
#     self.assertEqual(CustomUser.objects.count(), 1)
#     self.assertEqual(CustomUser.objects.get().email, "n@gmail.com")

# def test_validate_govi(self):
# def test_validate_email_uniqueness(self):
# # Create a user with an existing email
#     existing_email = "dwayne@gmail.com"
#     CustomUserFactory.create(email=existing_email)

#     self.data["email"] = existing_email

#     serializer = RegistrationSerializer(data=self.data)
#     # self.assertFalse(serializer.is_valid())
#     # print(serializer.errors)
#     # self.assertEqual(serializer.errors["email"][0], "Email already exists.")

#     # Create a user with a new email
#     new_email = "new@example.com"
#     self.data["email"] = new_email

#     serializer = RegistrationSerializer(data=self.data)
#     self.assertTrue(serializer.is_valid())
