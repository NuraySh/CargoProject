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
    if not re.match('^\d{8}$', value) and not re.match('^\d{7}$', value) and not re.match('^\d{5,6}$', value):
        raise ValidationError(_("The gov_id length is not correct"))
    


def validate_pin_code(value):
    if not re.match('^\w{7}$', value) or not re.match('^[A-Za-z0-9_-]*$', value):
        raise ValidationError(
            _('Pin code should contain 7 digits')
        )
    