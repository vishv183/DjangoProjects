import csv
from io import StringIO
from django.shortcuts import render
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, request, viewsets, pagination
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Profile.serializer import UploadSerializer
from Watches.filters import BaseFilter
from laptop.serializer import LaptopSerializer
from laptop.models import Laptop
from django_filters import rest_framework as filters
import logging
from rest_framework import serializers

logger = logging.getLogger("user")

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class LaptopViewSet(viewsets.ModelViewSet):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = BaseFilter
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new laptop instance.",
        request_body=LaptopSerializer,
        responses={201: LaptopSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing laptop instance.",
        request_body=LaptopSerializer,
        responses={200: LaptopSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a laptop instance.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        logger.info(f'  user = {request.user.username}')
        return Response("GET API")

    def create(self, request, file_upload=None):
        file_uploaded = request.FILES.get('file_uploaded')
        file_uploaded_read = file_uploaded.read()
        decode_file = file_uploaded_read.decode("utf-8")
        file_object = StringIO(decode_file)
        print(f'type of file object is {file_object}')
        content_type = file_uploaded.content_type
        if content_type != 'text/csv':
            response = {"error": "Only CSV files are allowed."}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        print(type(content_type))

        csvFile = csv.DictReader(file_object)
        for line in csvFile:
            print(line['Screen'])
            print(line)
            laptop, created = Laptop.objects.update_or_create(
                laptop=line.get('Laptop'),
                defaults={
                    'status': line.get('Status'),
                    'brand': line.get('Brand'),
                    'model': line.get('Model'),
                    'cpu': line.get('CPU'),
                    'ram': line.get('RAM'),
                    'Storage': line.get('Storage'),
                    'storage_type': line.get('Storage type'),
                    'gpu': line.get('GPU'),
                    'touch': True if line.get('Touch', '') == "Yes" else False,
                    'screen': float(line.get('Screen', '0')) if line.get('Screen', '') != "" else None,
                    'price': line.get('Final Price', ''),
                    'created_at': line.get('created_at')
                }
            )
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)