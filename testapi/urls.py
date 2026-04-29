from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
urlpatterns = [
    path('immigrations/', ImmigrationsListCreateAPIView.as_view(), name='immigrations'),
    path('immigraions/<int:pk>/', ImmigrationsDetail.as_view(), name='immigrations-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login',),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('data/', UserDataView.as_view(), name='user_data')
]