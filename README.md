# MetaSync

Simple Python script that preserves metadata while converting videos from MOV to MP4 format. When iPhone-recorded videos are converted to MP4 for better compatibility with Android devices, the metadata (such as capture date, location, and camera settings) is often lost. MetaSync solves this problem by copying metadata from the original MOV file to the converted MP4 file.

## Features
- Extracts metadata from MOV files
- Transfers metadata to the corresponding MP4 files
- Supports batch processing of multiple video files
- Utilizes ExifTool for efficient metadata handling
- File extensions can be altered to work with other formats 

## Prerequisites
- Python 3.x installed
- [ExifTool](https://exiftool.org/) installed and accessible

## Installation
1. Download and install ExifTool from [https://exiftool.org/](https://exiftool.org/)
2. Add ExifTool to your system PATH or Project folder
3. Clone this repository or download the script
4. Install required dependencies (if any)

## Folder Structure
```
/MetaSync
├── OG       # Folder containing original MOV files
├── Conv     # Folder containing converted MP4 files
├── script.py  # Python script for metadata transfer
└── README.md  # Project documentation
```

## Usage
1. Place the original MOV files in the `OG/` folder
2. Place the converted MP4 files in the `Conv/` folder (ensuring filenames match except for the extension)
3. Run the script:
   ```sh
   python script.py
   ```
4. The script will copy metadata from each MOV file to its corresponding MP4 file

## Example
```
OG/
  video1.MOV
  video2.MOV
Conv/
  video1.mp4
  video2.mp4
```
Running `python script.py` will transfer metadata from `video1.MOV` → `video1.mp4` and `video2.MOV` → `video2.mp4`.

## Known Issues
- Even if the metadata syncing succeeds, the next file is processed only after the ExifTool timeout!

## License
This project is open-source under the MIT License.
