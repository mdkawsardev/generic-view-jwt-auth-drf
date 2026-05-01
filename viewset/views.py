from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from viewset.serializers import UserDataSerializer
from rest_framework.response import Response
from viewset.models import UserData
class UserViewset(viewsets.ViewSet):
    
    def list(self, request):
        queryset = UserData.objects.all()
        serializer = UserDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        set_data = UserDataSerializer(data=request.data)
        if set_data.is_valid():
            set_data.save()
            return Response({"message:": "Inserted data saved!", "new data": set_data.data})