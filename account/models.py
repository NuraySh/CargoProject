from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from account.managers import CustomUserManager
from account.helpers import id_gen
from django.core.exceptions import ValidationError


class PhonePrefix(models.Model):

    PREFIXES = [
        ('1', '+99455'),
        ('2', '+99450'),
        ('3', '+99451'),
        ('4', '+99470'),
        ('5', '+99477'),
        ('6', '+99499') ]

    prefix_number = models.CharField(max_length=1, blank=False, null=False, choices=PREFIXES, verbose_name='phone prefixes')

    def __str__(self):
        return self.prefix_number

class Warehouse(models.Model):
    BRANCHES = [
        ('1', 'Ganjlik'),
        ('2',  'Narimanov'), 
        ('3',  '20 January')
    ]
    name = models.CharField(max_length=1, choices=BRANCHES, blank=False, null=False)

class CustomUser(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=25, verbose_name='first name', blank=False)
    last_name = models.CharField(max_length=25, verbose_name='first name', blank=False)
    
    GENDER = [
        ('m', 'male'),
        ('f', 'female')

    ]
    gender = models.CharField(max_length=1, choices=GENDER)
   
    phone_prefix = models.ForeignKey(PhonePrefix, on_delete=models.CASCADE)
    phone  = models.CharField(max_length=7, blank=False)
    SERIES = [
        ('1', 'AZE'),
        ('2', 'AA'),
        ('3', 'MYI'),
        ('4', 'DYI')
    ]
    gov_id  = models.CharField(max_length=1, choices=SERIES, blank=False, unique=True)
    pin_code = models.CharField(max_length=7, blank=False, unique=True)
    client_code  = models.CharField(max_length=9, primary_key=True, default=id_gen, editable=False) #do we need to write 'unique = True'?
    monthly_expense = models.CharField(max_length=50)
    birth_date = models.DateField(blank=False)
    
    is_active  = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    
    branch = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()


    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')

        if len(phone) != 7:
            raise ValidationError(
                'Phone should contain 7 digits'
            )

    def clean(self):
        cleaned_data = super().clen()
        gov_id = cleaned_data.get('gov_id')
        pass 

    def clean(self):
        cleaned_data = super().clean()
        pin_code = cleaned_data.get('pin_code')

        if len(pin_code) != 7:
            raise ValidationError(
                'Pin code should contain 7 digits'
            )

    



