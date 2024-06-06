from django.urls import path
from Profile.views import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from Profile.views import CustomTokenObtainPairView, RegisterApi, UserListUpdateView, UserUpdateSView

from django.urls import path, include
from rest_framework import routers
from Profile.views import UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
urlpatterns = [
    path('', index, name='index'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterApi.as_view(), name='register'),
    # path('api/users/', UserListView.as_view(), name='user'),
    # path('api/update-user/<int:pk>/', UpdateUser.as_view(), name='UpdateUser'),
    path('user-update/', UserListUpdateView.as_view(), name='superuer'),
    path("user-update-serializer/", UserUpdateSView.as_view(), name='userupdate serializer'),
    path('', include(router.urls)),

]