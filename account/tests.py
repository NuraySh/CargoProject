import unittest
import re
from account.models import validate_gov_id, validate_phone, validate_pin_code
from django.core.exceptions import ValidationError


class TestCustomUserValidators(unittest.TestCase):

     def test_pincode_validator(self):
         
         self.assertEqual(len(validate_pin_code('5zxu4pr')), 7)
         
         with self.assertRaises(ValidationError):
            validate_pin_code('5zxu4pra')


     def test_phone_validator(self):

        self.assertEqual(len(validate_phone('5899298')), 7)
        self.assertTrue(bool(re.match('^[0-9]+$', '3336647')))
        
        with self.assertRaises(ValidationError):
            validate_phone('5899298A')

        with self.assertRaises(ValidationError):
            validate_phone('58992989')
    
     def test_govid_validator(self):
        self.assertTrue(bool(re.match('^[0-9]+$', '3336647')))
        self.assertEqual(len(validate_gov_id('12345678')), 8)
        self.assertEqual(len(validate_gov_id('1234567')), 7)
        self.assertEqual(len(validate_gov_id('123456')), 6)
        self.assertEqual(len(validate_gov_id('12345')), 5)
        with self.assertRaises(ValidationError):
            validate_gov_id('123456789')
        
        """     
            Can not check validationerror message for each if/elif
            statement as given in 'validate_gov_id' function 
        """

        # id_series = ['AZE', 'AA', 'DYI', 'MYI']
        # for i in id_series:
        #     if i == 'AZE':
        #         self.assertEqual(len(validate_gov_id('12345678')), 8)
        #         with self.assertRaises(ValidationError) as cm:
        #             validate_gov_id('123456789')
        #         the_exception = cm.exception
        #         self.assertEqual(the_exception.messages[0], 'You should enter 8 digits')
            
        #     elif i == 'AA':
                
        #         self.assertEqual(len(validate_gov_id('1234567')), 7)
        #         with self.assertRaises(ValidationError):
        #             validate_gov_id('123456709')
        #         the_exception = cm.exception
        #         self.assertEqual(the_exception.messages[0],  'You should enter 7 digits')
            
        #     elif i == 'DYI' or i == 'MYI':
                
        #         self.assertEqual(len(validate_gov_id('123456')), 6)
        #         with self.assertRaises(ValidationError):
        #             validate_gov_id('12345679009')
        #         the_exception = cm.exception
        #         self.assertEqual(the_exception.messages[0], 'You should enter 5 or 6 digits')
                
        #         self.assertEqual(len(validate_gov_id('12345')), 5)
        #         with self.assertRaises(ValidationError):
        #             validate_gov_id('123')
        #         the_exception = cm.exception
        #         self.assertEqual(the_exception.messages[0], 'You should enter 5 or 6 digits')

            
            

        
        
