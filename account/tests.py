import unittest
from account.models import validate_gov_id, validate_phone, validate_pin_code
from django.core.exceptions import ValidationError
from account.factories import CustomUserFactory




class TestCustomUserValidators(unittest.TestCase):
    
    def test_valid_phone_number(self):
        user = CustomUserFactory.build()
        
        self.assertTrue(user.phone.isdigit())
        self.assertEqual(len(user.phone), 7)

    def test_invalid_phone_number(self):
        user = CustomUserFactory.build(phone='abc')
        with self.assertRaises(ValidationError):
            validate_phone(user.phone)


    def test_valid_pin_code(self):
        
        user = CustomUserFactory.build()

        self.assertTrue(user.pin_code.isalnum())
        self.assertEqual(len(user.pin_code), 7)

    def test_invalid_pin_code(self):
        user = CustomUserFactory.build(pin_code='5zxu4pr_=')
        with self.assertRaises(ValidationError):
            validate_pin_code(user.pin_code)


    def test_validate_gov_id(self):
        # test with gov_id_prefix='AZE' and gov_id='12345678'
        user = CustomUserFactory.build(gov_id_prefix='AZE', gov_id='12345678')
        self.assertEqual(len(user.gov_id), 8)
        self.assertTrue(user.gov_id.isdigit())
        

        # test with gov_id_prefix='AA' and gov_id='1234567'
        user = CustomUserFactory.build(gov_id_prefix='AA', gov_id='1234567')
        self.assertEqual(len(user.gov_id), 7)
        self.assertTrue(user.gov_id.isdigit())

        # test with gov_id_prefix='MYI' and gov_id='12345'
        user = CustomUserFactory.build(gov_id_prefix='MYI', gov_id='12345')
        self.assertEqual(len(user.gov_id), 5)
        self.assertTrue(user.gov_id.isdigit())

        # test with gov_id_prefix='DYI' and gov_id='123456'
        user = CustomUserFactory.build(gov_id_prefix='DYI', gov_id='123456')
        self.assertEqual(len(user.gov_id), 6)
        self.assertTrue(user.gov_id.isdigit())


    def test_invalid_gov_id(self):
        user = CustomUserFactory.build(gov_id_prefix='MYI', gov_id='1234567')
        with self.assertRaises(ValidationError):
            validate_gov_id(user.gov_id, user.gov_id_prefix)
