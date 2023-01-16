import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#model validators
def validate_phone(value):
    if not re.match('^[0-9]+$', value) or len(value) != 7:
        raise ValidationError(
            _('Phone should be numbers and 7 digits')
        )
    return value

def validate_gov_id(value):

   prefix = CustomUser.gov_id_prefix.field.choices
   gov_id_len = [8, 7, 6, 5]
   if re.match('^[0-9]+$', value):
    for choice in prefix:
        errors = []
        if len(value) not in gov_id_len and choice[1] == "AZE":
            errors.append(ValidationError(
            _('You should enter 8 digits'), code='error1'
        ))
    
        elif len(value) not in gov_id_len and choice[1] == "AA":

            errors.append(ValidationError(
            _('You should enter 7 digits'), code='error2'
        ))
        
        elif len(value) not in gov_id_len and (choice[1] == "MYI" or choice[1] == 'DYI'):

            errors.append(ValidationError(
            _('You should enter 5 or 6 digits'), code='error3'
        ))
           
        if errors:
            raise ValidationError(errors)
           
    return value

def validate_pin_code(value):
    if len(value) != 7:
        raise ValidationError(
            _('Pin code should contain 7 digits')
        )
    return value