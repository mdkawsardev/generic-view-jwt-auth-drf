from rest_framework import serializers
from user.models import UserDetails
from django.contrib.auth.models import User

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = "__all__"

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user