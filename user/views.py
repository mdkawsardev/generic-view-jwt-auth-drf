from django.shortcuts import render
from rest_framework import generics
from user.serializers import UserDetailsSerializer
from user.models import UserDetails

class UserDetailsView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserDetailsOpView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
