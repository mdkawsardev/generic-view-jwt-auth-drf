from django.urls import path
from user.views import UserDetailsView, UserDetailsOpView
urlpatterns = [
    path('data/', UserDetailsView.as_view(), name='user_details'),
    path('data/<int:pk>', UserDetailsOpView.as_view(), name='user_details'),
]
