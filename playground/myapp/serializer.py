from rest_framework import serializers
from .models import Convertedfiles

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convertedfiles
        fields = ['id', 'original_file', 'converted_file', 'file_name', 'file_size', 'file_format', 'is_converted', 'uploaded_at', 'converted_at']  # or specify specific f