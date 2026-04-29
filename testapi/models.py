from django.db import models

class Immigrations(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Passport_number = models.IntegerField()