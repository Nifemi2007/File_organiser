from pathlib import Path
import functions
FOLDER_NAME = "scattered_folder"

folder = Path(FOLDER_NAME)

try:
    functions.get_file_extension(folder)
    functions.create_storage_folder()
    functions.sort_file(folder)

except Exception as e:
    print(f"Error: {str(e)}")