import sys
import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_jpg(pdf_path, output_folder, quality=70, dpi=200):
    """
    Converts a PDF file to JPEG images, one image per page.
    
    Args:
        pdf_path (str): Path to the PDF file.
        output_folder (str): Directory to save the resulting JPEG images.
        quality (int): JPEG compression quality (1-100)
        dpi (int): DPI for converting PDF pages to images..
        
    Usage:
        py pdf_to_jgp.py pdf_input_path/                      [OR]
        py pdf_to_jgp.py pdf_input_path/ jpg_output_path/            [OR]
        py pdf_to_jgp.py pdf_input_path/ jpg_output_path/ 70         [OR]
        py pdf_to_jgp.py pdf_input_path/ jpg_output_path/ 70 200     [OR]
    """
    
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file '{pdf_path}' not found.")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(f"Converting '{pdf_path}' to images...")
    pages = convert_from_path(pdf_path, dpi=dpi)
    
    for i, page in enumerate(pages):
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        image_name = f"{pdf_name}.jpg"
        output_path = os.path.join(output_folder, image_name)
        
        page.save(output_path, "JPEG", quality=quality)
        print(f"Saved: {output_path}")

    print(f"PDF '{pdf_path}' successfully converted and saved in '{output_folder}'.")

def process_folder(input_folder, output_folder="output_folder", quality=70, dpi=200):
    """
    Processes all PDF files in the input folder and converts them to JPEGs.
    
    Args:
        input_folder (str): Folder containing PDF files.
        output_folder (str): Folder to save the JPEG images.
        quality (int): JPEG quality.
        dpi (int): DPI for conversion.
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' not found.")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_to_jpg(pdf_path, output_folder, quality=quality, dpi=dpi)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_jpg.py <input_folder> [output_folder] [dpi] [quality]")
        print(" - <input_folder>: Folder containing PDF files.")
        print(" - [output_folder]: (Optional) Folder to save the JPEG images (default: 'output_folder').")
        print(" - [quality]: (Optional) JPEG quality (default: 70).")
        print(" - [dpi]: (Optional) DPI for conversion (default: 200).")
        sys.exit(1)

    try:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_folder"
        quality = int(sys.argv[3]) if len(sys.argv) > 3 else 70
        dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 200

        process_folder(input_folder, output_folder, dpi=dpi, quality=quality)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
