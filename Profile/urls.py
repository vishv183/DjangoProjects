from django.urls import path
from Profile.views import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from Profile.views import CustomTokenObtainPairView, RegisterApi, UserListUpdateView, AudioToTextView

from django.urls import path, include
from rest_framework import routers
from Profile.views import UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
urlpatterns = [
    path('home/', index, name='index'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterApi.as_view(), name='register'),
    # path('api/users/', UserListView.as_view(), name='user'),
    # path('api/update-user/<int:pk>/', UpdateUser.as_view(), name='UpdateUser'),
    path('api/user-update/', UserListUpdateView.as_view(), name='superuer'),
    path('convert/', AudioToTextView.as_view()),
    path('', include(router.urls)),

]