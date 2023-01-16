from core.models import News, Country
from core.api.serializers import NewsSerializer, CountrySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NewsList(APIView):
    """
    List all news, or create a new news.
    """
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class CountryList(APIView):

     def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
