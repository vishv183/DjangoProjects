from django.urls import path, include
from rest_framework import routers

from laptop.views import  UploadViewSet, LaptopViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload"),
router.register(r'api', LaptopViewSet, basename='laptops')
urlpatterns = [

    path('', include(router.urls)),
]