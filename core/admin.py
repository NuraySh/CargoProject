from django.contrib import admin
from core.models import NewsCategory, News, Country, ContactUs, Currency, ProductType

# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(ProductType)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'work_hours',)
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
