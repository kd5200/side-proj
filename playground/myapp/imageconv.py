from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def convert_image(input_file, output_format):
    """
    Convert an image to another format.

    Parameters:
    - input_file: The input file to be converted (Django's File object).
    - output_format: The desired output format (e.g., 'JPEG', 'PNG', etc.).

    Returns:
    - Converted file (Django's File object) if successful, None otherwise.
    """
    try:
        # Open the input image
        image = Image.open(input_file)
        
        # Create a BytesIO object to hold the converted image data
        output_buffer = BytesIO()
        
        # Convert the image to the specified format and save it to the buffer
        image.save(output_buffer, format=output_format)
        
        # Create a Django ContentFile from the buffer data
        converted_file = ContentFile(output_buffer.getvalue())
        
        return converted_file
    except Exception as e:
        # Handle exceptions (e.g., unsupported file format, invalid input)
        print(f"Error converting image: {e}")
        return None