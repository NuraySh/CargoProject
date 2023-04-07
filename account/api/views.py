from account.models import PhonePrefix
from account.api.serializers import PhonePrefixSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PhonePrefixList(APIView):
    """
    List all news, or create a new news.
    """
    def get(self, request, format=None):
        phoneprefix = PhonePrefix.objects.all()
        serializer = PhonePrefixSerializer(phoneprefix, many=True)
        return Response(serializer.data)
