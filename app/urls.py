from django.urls import path
from .views import *
urlpatterns = [
    path('privacy/', privacy, name='Privacy'),
]