from django.contrib import admin
from declaration.models import PackageDeclaration, PackageStatus, PackageStatusHistory

@admin.register(PackageDeclaration)
class PackageDeclarationAdmin(admin.ModelAdmin):
    list_display = ('user', 'tracking_code', )


@admin.register(PackageStatus)
class PackageStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)

@admin.register(PackageStatusHistory)
class PackageStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_changed', )
