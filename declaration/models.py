from django.db import models
from core.models import Discount, CustomUser, Currency, Country, LocalWarehouse, ProductType

class PackageDeclaration(models.Model):

    PACKAGE_STATUS = [
        ('FW', 'Foreign Warehouse'),
        ( 'LW', 'Local Warehouse'),
    ]
    tracking_code = models.CharField(max_length=50, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=PACKAGE_STATUS) #if the approach is right?
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    destination_warehouse = models.ForeignKey(LocalWarehouse, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.ManyToManyField(Discount, related_name='declarations', blank=True)
    is_liquid = models.BooleanField(default=False)
    shop_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='declarations/')
    image = models.ImageField(upload_to='declarations/')
    quantity = models.PositiveIntegerField()
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


