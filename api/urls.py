from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='About'),
    path('studentslist/', GetAllStudentsAPIview.as_view(), name='studentList'),
    path('studentslist/<int:pk>/', GetAllStudentsAPIview.as_view()),
    path('studentsdata/', StudentsListAPIview.as_view(), name='student-data'),
    path('studentsdata/', StudentsListAPIview.as_view(), name='student-data'),
]
urlpatterns = format_suffix_patterns(urlpatterns)