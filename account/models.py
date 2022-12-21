from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from django.utils.crypto import get_random_string
from .managers import CustomUserManager

def id_gen():
    return get_random_string(8, allowed_chars='0123456789')

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
    PREFIXES = [
        ('1', '+99455'),
        ('2', '+99450'),
        ('3', '+99451'),
        ('4', '+99470'),
        ('5', '+99477'),
        ('6', '+99499')
    ]
    phone_prefix = models.CharField(max_length=1, choices=PREFIXES, blank=False)
    phone  = models.CharField(max_length=7, blank=False)
    SERIES = [
        ('1', 'AZE'),
        ('2', 'AA')
    ]
    gov_id  = models.CharField(max_length=1, choices=SERIES, blank=False, unique=True)
    pin_code = models.CharField(max_length=6, blank=False, unique=True)
    client_code  = models.CharField(max_length=9, primary_key=True, default=id_gen, editable=False) #do we need to write 'unique = True'?
    monthly_expense = models.CharField(max_length=50)
    birth_date = models.DateField(blank=False)
    
    is_active  = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    
    BRANCHES = [
        ('1', 'Ganjlik'),
        ('2',  'Narimanov'), 
        ('3',  '20 January')
    ]
    branch = models.CharField(max_length=1, choices=BRANCHES)


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


    




