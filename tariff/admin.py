from django.contrib import admin
from tariff.models import PackageCost, PenaltyTariff
# Register your models here.
admin.site.register(PackageCost)
admin.site.register(PenaltyTariff)