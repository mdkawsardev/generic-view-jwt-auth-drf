from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import *
urlpatterns = [
    path('data/', UserDetailsView.as_view(), name='user_details'),
    path('data/<int:pk>', UserDetailsOpView.as_view(), name='user_details'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
