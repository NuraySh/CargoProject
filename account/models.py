import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.helpers import id_gen
from account.managers import CustomUserManager
from account.validators import validate_phone, validate_pin_code


class PhonePrefix(models.Model):
    PREFIXES = [
        ("+99455", "+99455"),
        ("+99450", "+99450"),
        ("+99451", "+99451"),
        ("+99470", "+99470"),
        ("+99477", "+99477"),
        ("+99499", "+99499"),
    ]

    prefix_number = models.CharField(max_length=6, choices=PREFIXES)

    def __str__(self):
        return self.prefix_number


class Warehouse(models.Model):
    BRANCHES = [("GN", "Ganjlik"), ("NR", "Narimanov"), ("20Jan", "20 January")]
    name = models.CharField(max_length=5, choices=BRANCHES, blank=False, null=False)

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True, null=True
    )
    first_name = models.CharField(max_length=25, verbose_name="first name")
    last_name = models.CharField(max_length=25, verbose_name="last name")

    GENDER = [("m", "male"), ("f", "female")]

    gender = models.CharField(max_length=1, choices=GENDER)

    phone_prefix = models.ForeignKey(
        PhonePrefix, on_delete=models.CASCADE, null=True, blank=True
    )
    phone = models.CharField(max_length=7, validators=[validate_phone])

    SERIES = [("AZE", "AZE"), ("AA", "AA"), ("MYI", "MYI"), ("DYI", "DYI")]

    gov_id_prefix = models.CharField(max_length=3, choices=SERIES, default="AZE")
    gov_id = models.CharField(max_length=8, unique=True)
    pin_code = models.CharField(
        max_length=7, unique=True, validators=[validate_pin_code]
    )
    client_code = models.CharField(
        max_length=9, primary_key=True, default=id_gen, editable=False
    )
    monthly_expense = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    birth_date = models.DateField(null=True)
    branch = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["birth_date"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()

        regex1 = "^\d{8}$"
        regex2 = "^\d{7}$"
        regex3 = "^(?:\d{5}|\d{6})$"
        validators = {"AZE": regex1, "AA": regex2, "MYI": regex3, "DYI": regex3}
        prefix = self.gov_id_prefix

        if re.match("^[0-9]+$", self.gov_id):
            if not re.match(validators[prefix], self.gov_id):
                raise ValidationError("Please enter right numbers of digits")
        else:
            raise ValidationError("All numbers have to be digit")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CustomUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
