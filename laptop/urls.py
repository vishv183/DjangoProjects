from django.urls import path, include
from rest_framework import routers

from laptop.views import GamingLaptopListCreateView, GamingLaptopRetrieveUpdateDestroyView, UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
urlpatterns = [
    path('gaming-laptops/', GamingLaptopListCreateView.as_view(), name='gaming-laptop-list-create'),
    path('gaming-laptops/<int:pk>/', GamingLaptopRetrieveUpdateDestroyView.as_view(), name='gaming-laptop-detail'),
    path('', include(router.urls)),

]