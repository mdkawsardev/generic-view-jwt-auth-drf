from viewset.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userdata', UserViewset, basename='user')
urlpatterns = router.urls
