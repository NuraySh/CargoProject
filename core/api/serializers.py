from rest_framework import serializers
from core.models import News, Country

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'category', 'image', 'detail', 'add_time', 'slug']
        



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'enabled']
