from django.urls import path
from user.views import UserDetailsView
urlpatterns = [
    path('data/', UserDetailsView.as_view(), name='user_details')
]
