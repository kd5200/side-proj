from rest_framework import viewsets
from .models import Convertedfiles
from .serializer import ModelSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Convertedfiles.objects.all()
    serializer_class = ModelSerializer