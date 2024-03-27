from django.db import models

class Convertedfiles(models.Model):
    # File conversion 
    original_file = models.FileField(upload_to="uploads/")
    converted_file = models.FileField(upload_to="converted/")

    # Conversion status
    is_converted = models.BooleanField(default=False)

    # Timestamps
    uploaded_at = models.DateTimeField(auto_now_add=True)
    converted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.file_name

# Create your models here.
