from django.urls import path

from Profile.views import index

urlpatterns = [
    path('', index, name='index')
]