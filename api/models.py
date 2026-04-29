from django.db import models

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.class_name

class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department

class Area(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    roll = models.IntegerField()
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
