import os
import shutil

def categorize_files(directory):
    categories = {
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "documents": [".pdf", ".docx", ".txt", ".tex"],
        "videos": [".mp4", ".mkv", ".avi", ".mov"],
        "archives": [".zip", ".rar", ".tar"],
        "code": [".py", ".java", ".html"],
        "executables": [".jar"]
    }
    
    categorized_files = {category: [] for category in categories}
    categorized_files["others"] = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                file_extension = os.path.splitext(entry.name)[1].lower()
                categorized = False
                for category, extensions in categories.items():
                    if file_extension in extensions:
                        categorized_files[category].append(entry.path)
                        categorized = True
                        break
                if not categorized:
                    categorized_files["others"].append(entry.path)

    return categorized_files

def move_files(directory, categorized_files):
    for category, files in categorized_files.items():
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        for file in files:
            shutil.move(file, os.path.join(category_folder, os.path.basename(file)))

# Example usage for the Downloads directory
home_directory = os.path.expanduser('~')
downloads_directory = os.path.join(home_directory, 'Downloads')

categorized_files = categorize_files(downloads_directory)
move_files(downloads_directory, categorized_files)
