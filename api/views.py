from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

class GetAllStudentsAPIview(APIView):
    def get(self, request, format=None):
        objects = Student.objects.all()
        serializers = StudentSerializers(objects, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    def post(self, request, format=None):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        obj = Student.objects.filter(id=pk).all()
        obj.delete()
        return Response({'message':'Success'})

class StudentsListAPIview(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StudentSerializers(queryset, many=True)
        return Response(serializer.data)