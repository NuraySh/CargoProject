import re

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import CustomUser, PhonePrefix, Warehouse
from account.tokens import account_activation_token


class PhonePrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonePrefix
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(), message="Email already exists."
            )
        ]
    )
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    phone_prefix = serializers.PrimaryKeyRelatedField(
        queryset=PhonePrefix.objects.all(),
    )
    branch = serializers.PrimaryKeyRelatedField(
        queryset=Warehouse.objects.all(),
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "gender",
            "phone_prefix",
            "phone",
            "gov_id_prefix",
            "gov_id",
            "pin_code",
            "birth_date",
            "branch",
        )

    def validate_first_name(self, value):
        if not re.match('^[A-Za-z]+$', value):
            raise serializers.ValidationError("First name should only include letters.")
        return value

    def validate_last_name(self, value):
        if not re.match('^[A-Za-z]+$', value):
            raise serializers.ValidationError("Last name should only include letters.")
        return value

    # def validate_phone(self, value):
    #     if not re.match("^[0-9]+$", value) or not re.match("^\d{7}$", value):
    #         raise serializers.ValidationError("Phone should be numbers and only 7 digits")
    #     return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
            phone_prefix=validated_data["phone_prefix"],
            branch=validated_data["branch"],
            phone=validated_data["phone"],
            gov_id_prefix=validated_data["gov_id_prefix"],
            gov_id=validated_data["gov_id"],
            pin_code=validated_data["pin_code"],
            birth_date=validated_data["birth_date"],
            is_active=False,
        )

        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        current_site = get_current_site(self.context["request"])
        subject = "Activate your account"
        message = render_to_string(
            "registration/activation_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            },
        )
        from_email = "noreply@example.com"
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])
