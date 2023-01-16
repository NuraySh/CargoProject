from django.contrib import admin
from core.models import NewsCategory, News, Country
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)
# admin.site.register(Country)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled' )

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')
    prepopulated_fields = {"slug": ("title",)}
