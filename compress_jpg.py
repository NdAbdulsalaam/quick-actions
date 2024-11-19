import sys
import os
from PIL import Image

def compress_jpg(input_file, output_dir, quality=70):
    """
    Compress a single JPEG file and save it to the output directory.
    
    Args:
        input_file (str): Path to the input JPEG file.
        output_dir (str): Directory to save the compressed JPEG file.
        quality (int): JPEG compression quality (1-100, higher means better quality but larger file size).
        
    Usage:
        py compress_jpg.py jgp_input_path/                          [OR]
        py compress_jpg.py jgp_input_path/ jpg_output_path/         [OR]
        py compress_jpg.py jgp_input_path/ jpg_output_path/ 70      [OR]
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare output file path
    file_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, file_name)

    # Open and compress the image
    try:
        with Image.open(input_file) as img:
            # Ensure the image is in RGB mode for consistent JPEG compression
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Save the compressed image
            img.save(output_file, "JPEG", quality=quality)
            print(f"Compressed: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error compressing '{input_file}': {e}")

def process_folder(input_folder, output_folder="output_folder", quality=70):
    """
    Compress all JPEG files in a folder and save them to the output folder.
    
    Args:
        input_folder (str): Folder containing JPEG files to compress.
        output_folder (str): Directory to save the compressed JPEG files.
        quality (int): JPEG compression quality (1-100).
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' not found.")

    # Get all JPEG files in the input folder
    jpeg_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".jpg")]

    if not jpeg_files:
        print(f"No JPEG files found in '{input_folder}'.")
        return

    print(f"Compressing files in '{input_folder}'...")
    for jpeg_file in jpeg_files:
        input_file = os.path.join(input_folder, jpeg_file)
        compress_jpg(input_file, output_folder, quality=quality)

    print(f"All JPEG files compressed and saved in '{output_folder}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress_jpg.py <input_folder> [output_folder] [quality]")
        print(" - <input_folder>: Folder containing JPEG files to compress.")
        print(" - [output_folder]: (Optional) Directory to save the compressed files. Default: 'output_folder'.")
        print(" - [quality]: (Optional) JPEG quality (1-100). Default: 70.")
        sys.exit(1)

    try:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_folder"
        quality = int(sys.argv[3]) if len(sys.argv) > 3 else 70

        process_folder(input_folder, output_folder, quality)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
