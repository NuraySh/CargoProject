import factory
from account.models import CustomUser
from faker import Faker

fake = Faker()
class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        exclude = ('branch_id', 'phone_prefix_id',)
        model = CustomUser
        # django_get_or_create = ('gov_id_prefix', 'pin_code', 'phone', )

    gov_id_prefix = 'AZE'    
    phone = '5899298'
    pin_code = factory.LazyAttribute(lambda _: fake.lexify(text='???????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'))
   
