from django.contrib import admin
from core.models import NewsCategory, News
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')
    prepopulated_fields = {"slug": ("title",)}
