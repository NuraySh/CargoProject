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

class PenaltyTariff(models.Model):
    FIXED_OR_PERCENTAGE_CHOICES = [
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage'),
    ]
    starting_from = models.DateField()
    till = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fixed_or_percentage = models.CharField(max_length=10, choices=FIXED_OR_PERCENTAGE_CHOICES)

    class Meta:
        verbose_name = 'Penalty Tariff'
        verbose_name_plural = 'Penalty Tariffs'

    def __str__(self):
        return f"{self.starting_from} - {self.till}: {self.amount} '' ({self.fixed_or_percentage})"
