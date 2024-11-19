import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_file, output_dir):
    """
    Compress a single PDF file and save it to the output directory.

    Args:
        input_file (str): Path to the input PDF file.
        output_dir (str): Directory to save the compressed PDF file.
        
    Usage:
        py compress_pdf.py pdf_input_path/                          [OR]
        py compress_pdf.py pdf_input_path/ pdf_output_path/         [OR]
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare output file path
    file_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, file_name)

    try:
        # Read the PDF
        reader = PdfReader(input_file)
        writer = PdfWriter()

        # Add pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add metadata
        if reader.metadata:
            writer.add_metadata(reader.metadata)

        # Write the compressed PDF to the output file
        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"Compressed: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error compressing '{input_file}': {e}")

def process_folder(input_folder, output_folder="output_folder"):
    """
    Compress all PDF files in a folder and save them to the output folder.

    Args:
        input_folder (str): Folder containing PDF files to compress.
        output_folder (str): Directory to save the compressed PDF files.
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' not found.")

    # Get all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'.")
        return

    print(f"Compressing files in '{input_folder}'...")
    for pdf_file in pdf_files:
        input_file = os.path.join(input_folder, pdf_file)
        compress_pdf(input_file, output_folder)

    print(f"All PDF files compressed and saved in '{output_folder}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress_pdf.py <input_folder> [output_folder]")
        print(" - <input_folder>: Folder containing PDF files to compress.")
        print(" - [output_folder]: (Optional) Directory to save the compressed files. Default: 'output_folder'.")
        sys.exit(1)

    try:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_folder"

        process_folder(input_folder, output_folder)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)



# import sys
# import os
# from PyPDF2 import PdfReader, PdfWriter

# def compress_pdf(input_file, output_dir, compression_level=5):
#     """
#     Compress a single PDF file and save it to the output directory.
    
#     Args:
#         input_file (str): Path to the input PDF file.
#         output_dir (str): Directory to save the compressed PDF file.
#         compression_level (int): Placeholder for compression level (1-9). 
#                                  PyPDF2 doesn't directly support this, 
#                                  but the parameter is kept for extensibility.
                                 
#     Usage:
#         py compress_pdf.py pdf_input_path/                          [OR]
#         py compress_pdf.py pdf_input_path/ pdf_output_path/         [OR]
#         py compress_pdf.py pdf_input_path/ pdf_output_path/ 5       [OR]
#     """
#     if not os.path.exists(input_file):
#         raise FileNotFoundError(f"Input file '{input_file}' not found.")

#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Prepare output file path
#     file_name = os.path.basename(input_file)
#     output_file = os.path.join(output_dir, file_name)

#     # Read and compress the PDF
#     try:
#         reader = PdfReader(input_file)
#         writer = PdfWriter()

#         # Copy pages to the writer
#         for page in reader.pages:
#             writer.add_page(page)

#         # Add metadata and enable compression
#         writer.add_metadata(reader.metadata)
#         writer._header = b"%PDF-1.5"  # Use modern PDF version
#         writer.compress_content_streams()

#         # Write the compressed PDF to the output file
#         with open(output_file, "wb") as f:
#             writer.write(f)

#         print(f"Compressed: {input_file} -> {output_file}")
#     except Exception as e:
#         print(f"Error compressing '{input_file}': {e}")

# def process_folder(input_folder, output_folder="output_folder", compression_level=5):
#     """
#     Compress all PDF files in a folder and save them to the output folder.
    
#     Args:
#         input_folder (str): Folder containing PDF files to compress.
#         output_folder (str): Directory to save the compressed PDF files.
#         compression_level (int): Compression level placeholder (1-9).
#     """
#     if not os.path.exists(input_folder):
#         raise FileNotFoundError(f"Input folder '{input_folder}' not found.")

#     # Get all PDF files in the input folder
#     pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

#     if not pdf_files:
#         print(f"No PDF files found in '{input_folder}'.")
#         return

#     print(f"Compressing files in '{input_folder}'...")
#     for pdf_file in pdf_files:
#         input_file = os.path.join(input_folder, pdf_file)
#         compress_pdf(input_file, output_folder, compression_level=compression_level)

#     print(f"All PDF files compressed and saved in '{output_folder}'.")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python compress_pdf.py <input_folder> [output_folder] [compression_level]")
#         print(" - <input_folder>: Folder containing PDF files to compress.")
#         print(" - [output_folder]: (Optional) Directory to save the compressed files. Default: 'output_folder'.")
#         print(" - [compression_level]: (Optional) Placeholder for compression level (1-9). Default: 5.")
#         sys.exit(1)

#     try:
#         input_folder = sys.argv[1]
#         output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_folder"
#         compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 5

#         process_folder(input_folder, output_folder, compression_level)
#     except Exception as e:
#         print(f"Error: {e}")
#         sys.exit(1)
