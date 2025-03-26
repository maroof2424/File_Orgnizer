import os
import shutil

# Define the source folder (Change this to your desired folder)
SOURCE_FOLDER = "C:\\Users\\YourUsername\\Downloads"

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".7z"],
    "Programs": [".exe", ".msi", ".sh", ".bat"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".c", ".cpp"]
}

def organize_files():
    """Organize files in the source folder into categorized subfolders."""
    if not os.path.exists(SOURCE_FOLDER):
        print("❌ Source folder not found!")
        return

    # Iterate through files in the source folder
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_ext = os.path.splitext(file)[1].lower()

        # Determine the target category
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                target_folder = os.path.join(SOURCE_FOLDER, category)

                # Create the category folder if it doesn't exist
                os.makedirs(target_folder, exist_ok=True)

                # Move file to the correct folder
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"📂 Moved {file} → {category}")
                break

if __name__ == "__main__":
    organize_files()
    print("✅ File organization complete!")
