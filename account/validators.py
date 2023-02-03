import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#model validators
def validate_phone(value):
    if not re.match('^[0-9]+$', value) or not re.match('^\d{7}$', value):
        raise ValidationError(
            _('Phone should be numbers and 7 digits')
        )
        
def validate_gov_id(value):

    prefixes = ['AZE', 'AA', 'MYI', 'DYI']
    
    if re.match('^[0-9]+$', value):
        for choice in prefixes:
            if re.match('^(AZE)$', choice) and re.match('^\d{8}$', value):
                break
            elif re.match('^(AA)$', choice) and re.match('^\d{7}$', value):
                break
            elif re.match('^(MYI)$', choice) and re.match('^\d{5}:\{6}$', value):
                break
            elif re.match('^(DYI)$', choice) and re.match('^\d{5}:\{6}$', value):
                break
            else:
                raise ValidationError(_('Enter right digit'))
            


def validate_pin_code(value):
    if  not re.match('^\w{7}$', value) or not re.match('^[A-Za-z0-9_-]*$', value):
        raise ValidationError(
            _('Pin code should contain 7 digits')
        )
    