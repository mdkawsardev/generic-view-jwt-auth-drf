from rest_framework import serializers
from .models import *
class ClassSerializers(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = ["class_name"]

class AreaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Area
        exclude = ["id"]

class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude = ["id"]


class StudentSerializers(serializers.ModelSerializer):
    class_name = ClassSerializers()
    city = AreaSerializers()
    department = DepartmentSerializers()
    class Meta:
        model = Student
        fields = "__all__"
    def create(self, validated_data):
        class_data = validated_data.pop('class_name')
        city_data = validated_data.pop('city')
        dept_data = validated_data.pop('department')

        class_obj = Classes.objects.create(**class_data)
        city_obj = Area.objects.create(**city_data)
        dept_obj = Department.objects.create(**dept_data)

        student = Student.objects.create(class_name=class_obj, city=city_obj, department=dept_obj, **validated_data)
        return student