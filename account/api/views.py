from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers import (PhonePrefixSerializer,
                                     RegistrationSerializer)
from account.models import CustomUser, PhonePrefix
from account.tokens import (AccountActivationTokenGenerator,
                            account_activation_token)


class RegisterView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class PhonePrefixList(APIView):
    """
    List all news, or create a new news.
    """

    def get(self, request, format=None):
        phoneprefix = PhonePrefix.objects.all()
        serializer = PhonePrefixSerializer(phoneprefix, many=True)
        return Response(serializer.data)

class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        token_generator = AccountActivationTokenGenerator()

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            # return redirect('/login/')
            return Response({'detail': 'Account activated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Activation link is invalid or has expired'}, status=status.HTTP_400_BAD_REQUEST)

