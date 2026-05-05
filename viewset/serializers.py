from rest_framework import serializers
from viewset.models import *
from django.contrib.auth.models import User

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        # exclude = ["id"] it displays all data without id
        fields = "__all__"
class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
