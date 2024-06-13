from django.urls import path
from Watches.views import index, WatchListAPIView, unique_companies

urlpatterns = [
    path('',index, name='watches' ),
    path('api/', WatchListAPIView.as_view(), name='watches'),
    path('unique-brands/', unique_companies, name='unique_companies'),
]