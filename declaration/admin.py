from django.contrib import admin
from declaration.models import PackageDeclaration, PackageStatus

@admin.register(PackageDeclaration)
class PackageDeclarationAdmin(admin.ModelAdmin):
    list_display = ('user', 'tracking_code', )


@admin.register(PackageStatus)
class PackageStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
