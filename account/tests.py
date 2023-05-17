import re
import unittest

import django
from django.core.exceptions import ValidationError

from account.factories import CustomUserFactory
from account.models import CustomUser


class TestCustomUserValidators(django.test.TestCase):
    def test_valid_user_creation(self):
        user = CustomUserFactory()
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_phone_valid_user_creation(self):
        user = CustomUserFactory(phone="5899298")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_phone_invalid_user_creation_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(phone="589929")

    def test_phone_invalid_user_creation_alldigit(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(phone="5899d9")

    def test_pincode_valid_user_creation(self):
        user = CustomUserFactory(pin_code="5zxu4pf")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_invalid_user_creation_pincode_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(pin_code="5zxu4pst")

    def test_govid_valid_user_creation_govid_AZE(self):
        user = CustomUserFactory(gov_id_prefix="AZE", gov_id="12345678")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_gov_id_invalid_user_creation_govid_AZE_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="AZE", gov_id="1234567")

    def test_gov_id_invalid_user_creation_govid_AZE_alldigit(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="AZE", gov_id="123456f")

    def test_govid_valid_user_creation_govid_AA(self):
        user = CustomUserFactory(gov_id_prefix="AA", gov_id="1234567")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_gov_id_invalid_user_creation_govid_AA_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="AA", gov_id="12345678")

    def test_gov_id_invalid_user_creation_govid_AA_alldigit(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="AA", gov_id="12345B7")

    def test_govid_valid_user_creation_govid_MYI(self):
        user = CustomUserFactory(gov_id_prefix="MYI", gov_id="12355")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_gov_id_invalid_user_creation_govid_MYI_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="MYI", gov_id="1234567")

    def test_gov_id_invalid_user_creation_govid_MYI_alldigit(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="MYI", gov_id="123C45")

    def test_govid_valid_user_creation_govid_DYI(self):
        user = CustomUserFactory(gov_id_prefix="DYI", gov_id="12345")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)

    def test_gov_id_invalid_user_creation_govid_DYI_length(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="DYI", gov_id="1234567")

    def test_gov_id_invalid_user_creation_govid_DYI_alldigit(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(gov_id_prefix="DYI", gov_id="123C567")
