from django.contrib import admin
from viewset.models import UserData
@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "email"]
