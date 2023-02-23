import factory
from account.models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        exclude = ('branch_id', 'phone_prefix_id',)
        model = CustomUser
        # database = 'TEST_DB_NAME'

    gov_id_prefix = 'AZE'    
    # gov_id = '12345678'
    # pin_code = '5zxu4pr'
    phone = '5899298'
    birth_date = '1995-08-20'
    # branch_id = 4
    # phone_prefix_id = 7
    email = 'nshah@gmail.com'
