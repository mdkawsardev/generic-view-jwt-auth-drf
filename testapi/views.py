from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import ImmigrationSerializer, SignupSerializer

class ImmigrationsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Immigrations.objects.all()
    serializer_class = ImmigrationSerializer

class ImmigrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immigrations.objects.all()
    serializer_class = ImmigrationSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class UserDataView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        data = {
            "username": user.username,
            "email": user.email,
            "message": "Your private data!"
        }
        obj = Immigrations.objects.all()
        serializer = ImmigrationSerializer(obj, many=True)
        return Response({"Your credentials": data, "All data": serializer.data})
