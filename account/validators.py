import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#model validators
def validate_phone(value):
    if not re.match('^[0-9]+$', value) or not re.match('^\d{7}$', value):
        raise ValidationError(
            _('Phone should be numbers and 7 digits')
        )
    return value


def validate_gov_id(value):

    prefixes = ['AZE', 'AA', 'MYI', 'DYI']

    if re.match('^[0-9]+$', value):
        for choice in prefixes:
            if re.match('^(AZE)$', choice):
                if  not bool(re.match('^\d{8}$', value)):
                    raise ValidationError (
                    _('You should enter 8 digits')
                )
            elif bool(re.match('^(AA)$', choice)):
                if not re.match('^\d{7}$', value):
                    raise ValidationError (
                    _('You should enter 7 digits')
                )
            if bool(re.match('^(MYI)$', choice)):
                if not re.match('^\d{5}:\{6}$', value):
                    raise ValidationError (
                    _('You should enter 5 or 6 digits')
                )


def validate_pin_code(value):
    if not re.match('^\d{7}$', value) or not re.match('^[A-Za-z0-9_-]*$', value):
        raise ValidationError(
            _('Pin code should contain 7 digits')
        )
    return value
