from django.contrib import admin
from core.models import NewsCategory, News, Country, ContactUs, Currency, ForeignWarehouse,  LocalWarehouse,ProductType, FAQ, FAQ_Category, Discount 


admin.site.register(NewsCategory)
admin.site.register(ProductType)
admin.site.register(FAQ)
admin.site.register(FAQ_Category)


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

@admin.register(ForeignWarehouse)
class ForeignWarehouseAdmin(admin.ModelAdmin):
    list_display = ('country', 'address_header', )
@admin.register(LocalWarehouse)
class LocalWarehouseAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'address', 'active',)

@admin.register(Discount)
class DicountAdmin(admin.ModelAdmin):
    list_display = ('reason','constant_or_percentage', 'amount', )
    
    
