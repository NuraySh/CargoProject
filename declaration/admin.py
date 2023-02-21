from django.contrib import admin
from declaration.models import PackageStatus


@admin.register(PackageStatus)
class PackageStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
