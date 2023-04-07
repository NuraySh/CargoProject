from rest_framework import serializers
from account.models import PhonePrefix, CustomUser

class PhonePrefixSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = PhonePrefix
        fields = ['prefix_number']
