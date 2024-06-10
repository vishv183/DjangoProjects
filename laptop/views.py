import csv
from io import StringIO
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Profile.serializer import UploadSerializer
from laptop.serializer import GamingLaptopSerializer
from laptop.models import GamingLaptop


# Create your views here.

class GamingLaptopListCreateView(generics.ListCreateAPIView):
    queryset = GamingLaptop.objects.all()
    serializer_class = GamingLaptopSerializer


class GamingLaptopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GamingLaptop.objects.all()
    serializer_class = GamingLaptopSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
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

        # file_uploaded.decode("utf-8")
        csvFile = csv.DictReader(file_object)


        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
