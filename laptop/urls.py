from django.urls import path, include
from rest_framework import routers

from laptop.views import LaptopsListCreateView, LaptopsRetrieveUpdateDestroyView, UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
urlpatterns = [
    path('gaming-laptops/', LaptopsListCreateView.as_view(), name='gaming-laptop-list-create'),
    path('gaming-laptops/<int:pk>/', LaptopsRetrieveUpdateDestroyView.as_view(), name='gaming-laptop-detail'),
    path('', include(router.urls)),

]