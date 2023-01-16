import unittest
import re
from account.models import validate_gov_id, validate_phone, validate_pin_code
from django.core.exceptions import ValidationError


class TestCustomUserValidators(unittest.TestCase):

     def test_pincode_validator(self):
         
         self.assertEqual('5zxu4pr', '5zxu4pr')
         
         with self.assertRaises(ValidationError):
            validate_pin_code('5zxu4pra')


     def test_phone_validator(self):

        self.assertEqual(validate_phone('5899298'), '5899298')
        self.assertTrue(bool(re.match('^[0-9]+$', '3336647')))
        
        with self.assertRaises(ValidationError):
            validate_phone('5899298A')

        with self.assertRaises(ValidationError):
            validate_phone('58992989')
    
     def test_govid_validator(self):
        self.assertTrue(bool(re.match('^[0-9]+$', '3336647')))
        self.assertTrue(bool(re.match('^\d{8}$', '12345678')))
        self.assertTrue(bool(re.match('^\d{7}$', '1234567')))
        self.assertTrue(bool(re.match('^\d{6}$', '123456')))
        self.assertTrue(bool(re.match('^\d{5}$', '12345')))
        
        # don not raise error
        with self.assertRaises(ValidationError):
            validate_gov_id('12345')
        
        """     
            Can not check validationerror message for each if/elif
            statement as given in 'validate_gov_id' function 
        """

        
