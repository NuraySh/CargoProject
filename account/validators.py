import re 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser

def validate_phone(value):
    if not re.match('^[0-9]+$', value) or len(value) != 7:
        raise ValidationError(
             _('Phone should be numbers and 7 digits')
            )

def validate_gov_id(value):
    gov_id_prefix_choices = CustomUser.gov_id.field.choices 
    
    if re.match('^[0-9]+$', value):
        for choice in gov_id_prefix_choices:
            if choice[1] == 'AZE':
                if len(value) != 8:
                    raise ValidationError (
                        _( 'You should enter 8 digits')
                    )
            elif choice[1] == 'AA':
                if len(value) != 7:
                     raise ValidationError(
                'You should enter 7 digits')

            elif choice[1] == 'MYI' or choice[1] == 'DYI' :
                if len(value) != 5 or len(value) != 6:
                     raise ValidationError(
                'You should enter 5 or 6 digits')


def validate_pin_code(value):

    if len(value)!= 7:
        raise ValidationError (
            _('Pin code should contain 7 digits')
        )