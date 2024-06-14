from django.shortcuts import render
from django.http import HttpResponse
from django_filters import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Watches.filters import MyModelFilter, BaseFilter
from Watches.serializer import WatchSerializer
from Watches.models import Watch
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
# Create your views here.





@api_view(['GET'])
def unique_companies(request):
    unique_company_names = Watch.objects.values_list('brand', flat=True).distinct()
    return Response(unique_company_names)


class WatchListAPIView(generics.ListAPIView):
    queryset =  Watch.objects.all()
    serializer_class = WatchSerializer
    filter_backends = (filters.DjangoFilterBackend,OrderingFilter)
    filterset_class = MyModelFilter, BaseFilter



def index(request):
    return HttpResponse('Connected Sucessfully')
