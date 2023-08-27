from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from .models import User
from .validators import format_phone_number_to_e164


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ["id", "phone_number", "date_joined", "email", "first_name", "is_active", "is_staff", "is_superuser",
                  "last_login", "last_name", "password", "username"]
        read_only_fields = ['id', "date_joined", "last_login", "is_active", "is_staff", "is_superuser", "last_login"]

    def validate_phone_number(self, value):
        formatted_phone = format_phone_number_to_e164(value)
        if formatted_phone:
            return formatted_phone
        else:
            raise serializers.ValidationError('Invalid phone number format.')

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({"phone_number": "This phone number already exists."})
        return User.objects.create(**validated_data)
