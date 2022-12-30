from django.contrib import admin
from core.models import NewsCategory, News
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)