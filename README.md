# 🖼️ Image File Mover Script

This Python script moves image files from the Downloads folder (`~/Downloads`) to the Pictures folder (`~/Pictures`). Only files with specific extensions (`jpg`, `jpeg`, `png`) are moved.

## 📝 Description

1. **🔄 Change Directory**: The script changes the working directory to the user's Downloads folder.
2. **📁 List Files**: Lists all files in the current directory.
3. **🔍 Filter Extensions**: Identifies file extensions and filters out those that have image extensions.
4. **📂 Create Destination Folder**: If it does not exist, creates the user's Pictures folder.
5. **🚚 Move Files**: Moves files with specified extensions from the Downloads folder to the Pictures folder.

## ⚠️ Requirements

- No virtual environment needed as the script only uses Python’s standard libraries (`os` and `shutil`).

## 🚀 Usage

1. Ensure that the paths in the script (Downloads and Pictures folders) are correct and exist on your system.
2. Run the script in a compatible Python environment.
