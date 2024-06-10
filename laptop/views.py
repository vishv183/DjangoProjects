import csv
from io import StringIO
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Profile.serializer import UploadSerializer
from laptop.serializer import LaptopSerializer
from laptop.models import Laptop


# Create your views here.

class LaptopsListCreateView(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


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
        
        csvFile = csv.DictReader(file_object)
        for line in csvFile:
            print(line['Screen'])
            print(line)
            laptop = Laptop.objects.create(
                laptop=line.get('Laptop'),
                status=line.get('Status'),
                brand=line.get('Brand'),
                model=line.get('Model',),
                cpu=line.get('CPU',),
                ram=line.get('RAM',),
                Storage=line.get('Storage'),
                storage_type=line.get('Storage type'),
                gpu=line.get('GPU'),
                touch=True if line.get('Touch', '') == "Yes" else False,
                screen=float(line.get('Screen', '0')) if line.get('Screen', '') != "" else None,
                price=line.get('Final Price', '')
            )

        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
