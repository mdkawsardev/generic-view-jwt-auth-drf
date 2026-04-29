from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.serializers import *
from user.models import UserDetails
from django.contrib.auth.models import User


class UserDetailsOpView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class UserDetailsView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        data = {
            "message": "Your private data!",
            "username": user.username,
            "email": user.email,
        }
        obj = UserDetails.objects.all()
        serializer = UserDetailsSerializer(obj, many=True)
        return Response({
            "Your credentials": data,
            "All data": serializer.data
        })
