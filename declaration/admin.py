from django.contrib import admin
from declaration.models import PackageDeclaration

@admin.register(PackageDeclaration)
class PackageDeclarationAdmin(admin.ModelAdmin):
    list_display = ('user', 'tracking_code', )