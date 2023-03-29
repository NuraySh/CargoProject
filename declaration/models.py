from django.db import models
from django.utils import timezone
from core.models import Discount, CustomUser, Currency, Country, LocalWarehouse, ProductType

class PackageStatus(models.Model):
    status_name= models.CharField(max_length=100)
    next_status = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField()
    
    class Meta:
        verbose_name = 'Package Status'
        verbose_name_plural = 'Package Status'

    def __str__(self):
        return self.status_name
    
class PackageDeclaration(models.Model):
    tracking_code = models.CharField(max_length=50, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(PackageStatus, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    destination_warehouse = models.ForeignKey(LocalWarehouse, on_delete=models.CASCADE, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discounts = models.ManyToManyField(Discount, related_name='declarations', blank=True)
    is_liquid = models.BooleanField(default=False)
    shop_name = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='declarations/')
    image = models.ImageField(upload_to='declarations/')
    quantity = models.PositiveIntegerField(null=True)
    is_paid = models.BooleanField(default=False)
    penalty_status = models.BooleanField(default=False)
    penalty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    is_added_to_customs = models.BooleanField(default=False)
    is_user_declared = models.BooleanField(default=False)
    is_added_to_the_box = models.BooleanField(default=False)
    is_depeshed = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = 'Package Declaration'
        verbose_name_plural = 'Package Declarations'

    def __str__(self):
        return f'User: {self.user} - tracking code: {self.tracking_code}'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_status = self.status

    def save(self, *args, **kwargs):
        if self.pk is not None:
            if self.status != self.cache_status:
                status_history = PackageStatusHistory(package=self, status=self.status)
                status_history.save()

        super().save(*args, **kwargs)


class PackageStatusHistory(models.Model):
    package = models.ForeignKey(PackageDeclaration, on_delete=models.CASCADE)
    status = models.ForeignKey(PackageStatus, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Status History'
        verbose_name_plural = 'Status History'
        ordering = ['-date_changed']

    def __str__(self):
        return self.status