from rest_framework import serializers
from viewset.models import *
class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        exclude = ["id"]