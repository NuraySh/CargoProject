from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from account.managers import CustomUserManager
from account.helpers import id_gen
from django.core.exceptions import ValidationError


class PhonePrefix(models.Model):

    PREFIXES = [
        ('+99455', '+99455'),
        ('+99450', '+99450'),
        ('+99451', '+99451'),
        ('+99470', '+99470'),
        ('+99477', '+99477'),
        ('+99499', '+99499') ]

    prefix_number = models.CharField(max_length=6, blank=False, null=False, choices=PREFIXES, verbose_name='phone prefixes')

    def __str__(self):
        return self.prefix_number

class Warehouse(models.Model):
    BRANCHES = [
        ('GN', 'Ganjlik'),
        ('NR',  'Narimanov'), 
        ('20Jan',  '20 January')
    ]
    name = models.CharField(max_length=5, choices=BRANCHES, blank=False, null=False)

    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser,PermissionsMixin):
    
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
   
    phone_prefix = models.OneToOneField(PhonePrefix, on_delete=models.CASCADE, null=True)
    phone  = models.CharField(max_length=7, blank=False)
    SERIES = [
        ('1', 'AZE'),
        ('2', 'AA'),
        ('3', 'MYI'),
        ('4', 'DYI')
    ]
    gov_id  = models.CharField(max_length=12, choices=SERIES, blank=False, unique=True, default='AZE')
    pin_code = models.CharField(max_length=7, blank=True, null=True, unique=True)
    client_code  = models.CharField(max_length=9, primary_key=True, default=id_gen, editable=False) #do we need to write 'unique = True'?
    monthly_expense = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    birth_date = models.DateField(null=True)
   
    
    is_active  = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    branch = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)


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

    # @property
    # def is_staff(self):
    #     return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

        
    def clean_phone(self):
        
        phone = self.cleaned_data['phone']

        if len(phone) != 7:
            raise ValidationError(
                'Phone should contain 7 digits'
                )

        return phone



    def clean_pin_code(self):

        pin_code = self.cleaned_data['pin_code']

        if len(pin_code) != 7:
            raise ValidationError(
                'Pin code should contain 7 digits'
            )
        return pin_code

    def clean_gov_id(self):
        gov_id_choices = CustomUser.gov_id.field.choices 
        gov_id = self.cleaned_data['gov_id']
       
        for choice in gov_id_choices:
            if choice[1] == 'AZE':
                if len(gov_id) != 11:
                     raise ValidationError(
                'You should enter 8 digits')
            
            elif choice[1] == 'AA':
                if len(gov_id) != 9:
                     raise ValidationError(
                'You should enter 7 digits')

            elif choice[1] == 'MYI' or choice[1] == 'DYI' :
                if len(gov_id) != 5 or len(gov_id) != 6:
                     raise ValidationError(
                'You should enter 5 or 6 digits')
 





