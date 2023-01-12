from rest_framework import serializers
from core.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'category', 'image', 'detail', 'add_time', 'slug']