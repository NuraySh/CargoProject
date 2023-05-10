from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
import re
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
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    phone_prefix = serializers.PrimaryKeyRelatedField(
            queryset = PhonePrefix.objects.all(), 
        
        )
    branch = serializers.PrimaryKeyRelatedField(
            queryset = Warehouse.objects.all(), 
            
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

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = self.context.get("request").data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs 
    def validate_email(self, attrs):
        email = attrs.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})
        return attrs
    
    def validate_firstname(self, attrs):
        firstname = attrs.get("first_name")
        if not re.match('^[A-Za-z]+$', firstname):
            raise serializers.ValidationError({"first_name": "First name should only include letters."})
        return attrs
    
    def validate_lastname(self, attrs):
        lastname = attrs.get("last_name")
        if not re.match('^[A-Za-z]+$', lastname):
            raise serializers.ValidationError({"first_name": "First name should only include letters."})
        return attrs
    
    def validate_phone(self, attrs):
        phone = attrs.get("phone")
        if not re.match("^[0-9]+$", phone) or not re.match("^\d{7}$", phone):
            raise serializers.ValidationError({"phone": "Phone should be numbers and only 7 digits"})

    def validate_pincode(self, attrs):
        pincode = attrs.get("pincode")
        if not re.match("^\w{7}$", pincode) or not re.match("^[A-Za-z0-9_-]*$", pincode):
            raise serializers.ValidationError({"pin_code": "Pin code should only contain 7 digits"})

    def create(self, validated_data):
        password = validated_data.pop("password")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
            phone_prefix=validated_data['phone_prefix'],
            branch=validated_data['branch'],
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
