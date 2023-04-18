from django.contrib import admin

from account.models import CustomUser, PhonePrefix, Warehouse

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(PhonePrefix)
admin.site.register(Warehouse)
