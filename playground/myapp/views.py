from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from .imageconv import *
from rest_framework.renderers import JSONRenderer  # Import the appropriate renderer class


import os
import json

class ReactView(APIView):
    def get(self, request):
        # Retrieve data from the database and serialize it
        converted_files = Convertedfiles.objects.all()
        serializer = ModelSerializer(converted_files, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Initialize serializer with request data
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
def image_conv(request):
        renderer_classes = [JSONRenderer]

        input_file = request.FILES.get('input_file')
        output_format = request.POST.get('output_format')
        
        # Perform validation on input_file and output_format
        
        # Convert the image
        converted_file = convert_image(input_file, output_format)
        
        if converted_file:
            # Return the converted file
            return Response({'converted_file': converted_file}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to convert image'}, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
