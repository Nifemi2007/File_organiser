from pathlib import Path
import functions

FOLDER_NAME = "scattered_folder"

folder = Path(FOLDER_NAME)


functions.get_file_extension(folder)
functions.create_storage_folder()
functions.sort_file(folder)