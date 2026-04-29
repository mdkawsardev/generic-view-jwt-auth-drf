from django.db import models

class UserDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    passport_number = models.IntegerField()
    national_id = models.IntegerField()
