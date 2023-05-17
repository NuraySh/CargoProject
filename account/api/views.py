from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
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

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PhonePrefixList(APIView):
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
            return redirect("/api/login/")

        else:
            return Response(
                {"detail": "Activation link is invalid or has expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if not user.is_active:
                return Response(
                    {"error": "User account is not activated"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            authenticated_user = authenticate(email=email, password=password)

            if authenticated_user:
                token, created = Token.objects.get_or_create(user=authenticated_user)
                return Response({"token": token.key})
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
