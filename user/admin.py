from django.contrib import admin
from user.models import UserDetails

# admin.site.register(UserDetails)
@admin.register(UserDetails)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'nationality', 'passport_number', 'national_id']