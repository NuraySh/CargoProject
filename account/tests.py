import unittest
import re
from account.models import validate_gov_id, validate_phone, validate_pin_code
from django.core.exceptions import ValidationError
from account.factories import CustomUserFactory
import django
from account.models import CustomUser
class TestCustomUserValidators(django.test.TestCase):

     def test_valid_user_creation(self):
        user = CustomUserFactory.create(password = '1234')
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.is_active, False)
    
     def test_invalid_user_creation_phone(self):
         with self.assertRaises(ValidationError):
            CustomUserFactory.create(password = '1234', phone = '589929')

     def test_invalid_user_creation_pincode(self):
        with self.assertRaises(ValidationError):
            CustomUserFactory.create(password = '1234', pin_code = '5zxu4pst')

     def test_invalid_user_creation_govid(self):
         with self.assertRaises(ValidationError):
             CustomUserFactory.create(password = '1234', gov_id ='123456789')
         
     

