import sys
import os
import subprocess

def compress_pdf(input_file, output_dir, compression_level="screen"):
    """
    Compress a single PDF file using Ghostscript and save it to the output directory.

    Args:
        input_file (str): Path to the input PDF file.
        output_dir (str): Directory to save the compressed PDF file.
        compression_level (str): Ghostscript preset for compression. Options are:
            - 'screen': Low-resolution (72 dpi), smallest file size.
            - 'ebook': Medium resolution (150 dpi), smaller file size.
            - 'printer': High resolution (300 dpi), larger file size.
            - 'prepress': Very high resolution (up to 400 dpi), largest file size.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare output file path
    file_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, file_name)

    # Ghostscript command
    gs_command = [
        "gs",                 # Ghostscript executable
        "-sDEVICE=pdfwrite",  # Specify output device
        f"-dPDFSETTINGS=/{compression_level}",  # Compression level
        "-dCompatibilityLevel=1.4",  # Target PDF version
        "-dNOPAUSE",          # Do not prompt on each page
        "-dBATCH",            # Exit after processing
        "-dQUIET",            # Suppress output messages
        f"-sOutputFile={output_file}",  # Specify output file
        input_file            # Input file
    ]

    try:
        # Run Ghostscript command
        subprocess.run(gs_command, check=True)
        print(f"Compressed: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error compressing '{input_file}': {e}")

def process_folder(input_folder, output_folder="output_folder", compression_level="screen"):
    """
    Compress all PDF files in a folder and save them to the output folder.

    Args:
        input_folder (str): Folder containing PDF files to compress.
        output_folder (str): Directory to save the compressed PDF files.
        compression_level (str): Ghostscript preset for compression.
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
        compress_pdf(input_file, output_folder, compression_level=compression_level)

    print(f"All PDF files compressed and saved in '{output_folder}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress_pdf.py <input_folder> [output_folder] [compression_level]")
        print(" - <input_folder>: Folder containing PDF files to compress.")
        print(" - [output_folder]: (Optional) Directory to save the compressed files. Default: 'output_folder'.")
        print(" - [compression_level]: (Optional) Compression level. Options: 'screen', 'ebook', 'printer', 'prepress'. Default: 'screen'.")
        sys.exit(1)

    try:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_folder"
        compression_level = sys.argv[3] if len(sys.argv) > 3 else "screen"

        process_folder(input_folder, output_folder, compression_level)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
