from docx import Document
from io import BytesIO
from django.core.files.base import ContentFile

def convert_document(input_file, output_format):
    """
    Convert a document to another format.

    Parameters:
    - input_file: The input document file (Django's File object).
    - output_format: The desired output format ('docx', 'pdf', etc.).

    Returns:
    - Converted file (Django's File object) if successful, None otherwise.
    """
    try:
        # Open the input document
        document = Document(input_file)
        
        # Create a BytesIO object to hold the converted document data
        output_buffer = BytesIO()
        
        # Convert the document to the specified format and save it to the buffer
        if output_format == 'docx':
            document.save(output_buffer)
        elif output_format == 'pdf':
            pdf_path = "temp.pdf"
            document.save(pdf_path)
            output_buffer.write(open(pdf_path, "rb").read())
        else:
            return None
        
        # Create a Django ContentFile from the buffer data
        converted_file = ContentFile(output_buffer.getvalue())
        
        return converted_file
    except Exception as e:
        # Handle exceptions (e.g., unsupported file format, invalid input)
        print(f"Error converting document: {e}")
        return None