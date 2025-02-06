import os
import subprocess

# Base Folders
og_folder = "OG" #Place Original files here
conv_folder = "Conv" #Place Converted files here

# ExifTool path
exiftool_path = "exiftool(-k).exe"  # If using installed version, try just "exiftool"

def copy_metadata(mov_file, mp4_file):
    """Copy metadata from MOV to MP4 using ExifTool."""
    cmd = [
        exiftool_path,
        "-tagsFromFile", mov_file,  # Copy metadata
        "-overwrite_original",  # Usually -tagsFromFile creates a backup file! So this line Prevents creation of that!
        mp4_file
    ]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10) #Reduce timeout if you prefer :)
        if result.returncode == 0:
            print(f"Metadata copied: {mov_file} → {mp4_file}")
        else:
            print(f"Error copying metadata for {mp4_file}\nError: {result.stderr}")

    except subprocess.TimeoutExpired:
        print(f"Timeout: ExifTool took too long for {mp4_file}")
    except FileNotFoundError:
        print(f"Error: ExifTool not found. Check the path: {exiftool_path}")

def main():
    files_processed = 0
    mov_files = [f for f in os.listdir(og_folder) if f.lower().endswith(".mov")]

    if not mov_files:
        print("No MOV files found in OG folder!")
        return

    print(f"Found {len(mov_files)} MOV files to process.\n")

    for filename in mov_files:
        mov_file = os.path.join(og_folder, filename)
        mp4_file = os.path.join(conv_folder, filename[:-4] + ".mp4")

        if os.path.exists(mp4_file):
            copy_metadata(mov_file, mp4_file)
            files_processed += 1
        else:
            print(f"Skipping: No converted file for {filename}")

    print(f"\nSuccessfully processed {files_processed} files.")

if __name__ == "__main__":
    main()
