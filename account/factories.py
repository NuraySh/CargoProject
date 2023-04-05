import factory
from account.models import CustomUser, PhonePrefix, Warehouse
from faker import Faker

fake = Faker()

class PhonePrefixFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhonePrefix

    prefix_number = '+99477'


class WarehouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Warehouse

    name = 'GN'
    
class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        exclude = ('branch_id', 'phone_prefix_id',)
        model = CustomUser
        # django_get_or_create = ('gov_id_prefix', 'pin_code', 'phone', )

    # gov_id_prefix = 'AZE'   
    # gov_id = '1234567' 
    # phone = '5899298'
    # pin_code = factory.LazyAttribute(lambda _: fake.lexify(text='???????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'))
   
    email = factory.Sequence(lambda n: 'user{}@example.com'.format(n))
    first_name = 'John'
    last_name = 'Doe'
    gender = 'm'
    phone_prefix = factory.SubFactory(PhonePrefixFactory)
    phone = '1234567'
    gov_id_prefix = '1'
    gov_id = '12345678'
    pin_code = factory.LazyAttribute(lambda _: fake.lexify(text='???????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'))
    birth_date = '2000-01-01'
    branch = factory.SubFactory(WarehouseFactory)

    