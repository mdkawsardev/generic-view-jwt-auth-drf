from rest_framework import serializers
from user.models import UserDetails
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = "__all__"
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({"error": "Age under 18 is not preffered!"})
        return data

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user