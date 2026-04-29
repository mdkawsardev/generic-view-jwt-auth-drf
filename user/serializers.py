from rest_framework import serializers
from user.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = "__all__"