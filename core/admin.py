from django.contrib import admin
from core.models import NewsCategory, News, Country
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)
# admin.site.register(Country)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled' )
#     list_display_links = None
#     # list_filter = ('category', 'available')
#     # list_editable = ( 'name',)
    
    # prepopulated_fields = {'slug': ('name',)}