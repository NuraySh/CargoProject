import secrets
from django.db.models.signals import pre_save
from django.dispatch import receiver
from declaration.models import PackageDeclaration

@receiver(pre_save, sender=PackageDeclaration)
def generate_tracking_code(sender, instance, **kwargs):
    if not instance.tracking_code:
        while True:
            tracking_code = str(secrets.randbelow(10**10)).zfill(10)
            if not PackageDeclaration.objects.filter(tracking_code=tracking_code).exists():
                instance.tracking_code = tracking_code
                break