# File Organizer – Automatically Sort and Categorize Files

## Overview
This Python script automatically organizes files in a specified folder by categorizing them into subfolders based on file types (e.g., Images, Documents, Videos, Music, etc.).

## Features
✅ Scans a target directory (e.g., `Downloads` or `Desktop`).  
✅ Creates categorized folders (`Images`, `Documents`, `Videos`, etc.).  
✅ Moves files into the correct category based on their extensions.  

## Installation
1. Ensure you have Python installed (Python 3.x recommended).
2. Install required dependencies (optional for real-time monitoring):
   ```bash
   pip install watchdog
   ```

## Usage
1. Update the `SOURCE_FOLDER` variable in the script to the directory you want to organize.
2. Run the script:
   ```bash
   python file_organizer.py
   ```
3. The script will create categorized folders and move files accordingly.

## File Type Categories
| Category   | File Extensions |
|------------|----------------|
| Images     | .jpg, .jpeg, .png, .gif, .bmp, .svg |
| Documents  | .pdf, .docx, .txt, .xlsx, .pptx |
| Videos     | .mp4, .mkv, .avi, .mov |
| Music      | .mp3, .wav, .flac |
| Archives   | .zip, .rar, .tar, .7z |
| Programs   | .exe, .msi, .sh, .bat |
| Code       | .py, .java, .js, .html, .css, .c, .cpp |

## Future Enhancements
- **Real-time Monitoring**: Detect new files and organize them instantly.
- **Logging System**: Keep a log of moved files.
- **Undo Feature**: Store previous locations for undo functionality.


