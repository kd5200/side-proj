from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from .imageconv import *
from rest_framework.renderers import JSONRenderer  # Import the appropriate renderer class
import document as dc
from io import BytesIO
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# @renderer_classes([JSONRenderer])   
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated]) 
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
        

@api_view(['POST'])
@renderer_classes([JSONRenderer])   
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])     
def image_conv(request):
        # renderer_classes = [JSONRenderer]

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
        


# def convert_document(input_file, output_format):
#     """
#     Convert a document to another format.

#     Parameters:
#     - input_file: The input document file (Django's File object).
#     - output_format: The desired output format ('docx', 'pdf', etc.).

#     Returns:
#     - Converted file (Django's File object) if successful, None otherwise.
#     """
#     try:
#         # Open the input document
#         document = dc(input_file)
        
#         # Create a BytesIO object to hold the converted document data
#         output_buffer = BytesIO()
        
#         # Convert the document to the specified format and save it to the buffer
#         if output_format == 'docx':
#             document.save(output_buffer)
#         elif output_format == 'pdf':
#             pdf_path = "temp.pdf"
#             document.save(pdf_path)
#             output_buffer.write(open(pdf_path, "rb").read())
#         else:
#             return None
        
#         # Create a Django ContentFile from the buffer data
#         converted_file = ContentFile(output_buffer.getvalue())
        
#         return converted_file
#     except Exception as e:
#         # Handle exceptions (e.g., unsupported file format, invalid input)
#         print(f"Error converting document: {e}")
#         return None

# Create your views here.
