from django.urls import path
from Watches.views import index

urlpatterns = [
    path('',index, name='watches' )
]