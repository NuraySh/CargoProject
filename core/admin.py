from django.contrib import admin
from core.models import NewsCategory, News, Country, ProductType
from mptt.admin import MPTTModelAdmin
from core.models import NewsCategory, News, Country, Currency 
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(ProductType, MPTTModelAdmin)

@admin.register(Currency)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'rate', )

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled' )
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')
    prepopulated_fields = {"slug": ("title",)}
