from django.db import models
from core.models import Country

class PackageCost(models.Model):

    WEIGHT_TYPE = (
        ('fixed', 'Fixed'),
        ('per_unit', 'Per Unit'),
    )

    weight_from = models.DecimalField(max_digits=3, decimal_places=2)
    weight_to = models.DecimalField(max_digits=3, decimal_places=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    weight_type = models.CharField(choices=WEIGHT_TYPE, max_length=10)
    liquid = models.BooleanField()
    show_order = models.IntegerField()

    class Meta:
        verbose_name = 'Package Cost'
        verbose_name_plural = 'Package Costs'

    def __str__(self):
        return self.weight_type