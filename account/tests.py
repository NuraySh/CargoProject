import unittest
import re
from account.models import validate_gov_id, validate_phone, validate_pin_code
from django.core.exceptions import ValidationError


class TestCustomUserValidators(unittest.TestCase):

    #test for phone validation
     def test_phone_validator(self):

        self.assertEqual('5899298', '5899298')

        with self.assertRaises(ValidationError):
            validate_phone('58992989')
        with self.assertRaises(ValidationError):
            validate_phone('5899298a')
    
    #test for gov id validation
     def test_govid_validator(self):
        self.assertEqual('12345678','12345678')
        self.assertEqual('1234567', '1234567')
        self.assertEqual('123456', '123456')
        self.assertEqual('12345', '12345')
        
        with self.assertRaises(ValidationError):
            validate_gov_id('1234')
        

    # test for pin code validation
     def test_pincode_validator(self):
         
         self.assertEqual('5zxu4pr', '5zxu4pr')
         
         with self.assertRaises(ValidationError):
            validate_pin_code('5zxu4pr6')
         with self.assertRaises(ValidationError):
            validate_pin_code('5zxu4p-')

        
