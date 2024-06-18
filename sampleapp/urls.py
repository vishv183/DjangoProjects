from django.urls import path, include
from sampleapp.views import index
urlpatterns=[
    path('sample-app/', index)
]