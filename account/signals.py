import random
import string
from account.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver



@receiver(pre_save, sender=CustomUser)
def generate_client_code(sender, instance, **kwargs):
    if not instance.client_code:
        # Generate a 6-character string of uppercase letters and digits
        client_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Ensure the client code is unique
        while CustomUser.objects.filter(client_code=client_code).exists():
            client_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        instance.client_code = client_code