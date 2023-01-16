from django.contrib import admin
from core.models import NewsCategory, News, Country
# Register your models here.

admin.site.register(NewsCategory)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled' )
@admin.site.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')
    prepopulated_fields = {"slug": ("title",)}
