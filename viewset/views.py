from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from viewset.serializers import *
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from viewset.models import UserData
from rest_framework.permissions import IsAuthenticated

class UserViewset(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["name"]

class SignupViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer