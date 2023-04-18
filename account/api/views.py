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
from account.tokens import account_activation_token


class RegisterView(generics.CreateAPIView):
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


@api_view(["GET"])
def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response(
            {"message": "Account activated successfully"}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Invalid activation link"}, status=status.HTTP_400_BAD_REQUEST
        )
