import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#validator for phone field in CustomUser model
def validate_phone(value):
    if not re.match('^[0-9]+$', value) or not re.match('^\d{7}$', value):
        raise ValidationError(
            _('Phone should be numbers and 7 digits')
        )

#validator for gov_id field in CustomUser model 
def validate_gov_id(value, gov_id_prefix):
    if re.match('^[0-9]+$', value):
        if gov_id_prefix == 'AZE' and not re.match('^\d{8}$', value):
            raise ValidationError("The gov_id must be 8 characters long when gov_id_prefix is 'AZE'")
        elif gov_id_prefix == 'AA' and not re.match('^\d{7}$', value):
            raise ValidationError("The gov_id must be 7 characters long when gov_id_prefix is 'AA'")
        elif (gov_id_prefix == 'MYI' or gov_id_prefix == 'DYI') and not re.match('^\d{5,6}$', value):
            raise ValidationError("The gov_id must be 5 or 6 characters long when gov_id_prefix is 'MYI' or 'DYI'")

#validator for pin_code field in CustomUser model
def validate_pin_code(value):
    if  not re.match('^\w{7}$', value) or not re.match('^[A-Za-z0-9_-]*$', value):
        raise ValidationError(
            _('Pin code should contain 7 digits')
        )
    