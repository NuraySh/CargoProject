import factory
from factory import Sequence
from account.models import CustomUser
from itertools import cycle


class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = CustomUser

    gov_id = factory.Iterator(cycle(['12345','123456','1234567', '12345678']))
    # @factory.lazy_attribute
    # def gov_id(self):
    #     gov_id_len = ['12345','123456','1234567', '12345678']
    #     for i in range(len(gov_id_len)):
    #         return next(gov_id_len)
    gov_id_prefix = 'AZE'    
    gov_id = '12345678'
    pin_code = '5zxu4ps'
    phone = '5899298'
    