from django.db import models
from core.models import Currency, CustomUser, ProductType

class PackageDeclaration(models.Model):
    tracking_code = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ManyToManyField(Currency)
    status = models.BooleanField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    local_warehouse = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Package declaration'
        verbose_name_plural = 'Package declarations'

    def __str__(self):
        return f'{self.user} - {self.country} - {self.local_warehouse}'
