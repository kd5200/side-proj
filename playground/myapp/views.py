from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
import os
import json

class ReactView(APIView):
    def get(self, request):
        output = [{"original_file": output.original_file,
                   "converted_file": output.converted_file}
                   for output in Convertedfiles.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = serializers.ModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

# Create your views here.
