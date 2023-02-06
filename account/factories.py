import factory
from account.models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = CustomUser

    gov_id_prefix = 'AZE'    
    gov_id = '12345678'
    pin_code = '5zxu4ps'
    phone = '5899298'
    