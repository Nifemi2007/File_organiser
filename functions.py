from pathlib import Path
import shutil

organised = Path("Organised_files")
organised.mkdir(exist_ok= True)


file_extension = []


# Extract available file extensions

def get_file_extension(folder_name):
    for file in folder_name.iterdir():
        if file.is_file():
            file_extension.append(file.suffix)
        
    


# Create folder to store files
def create_storage_folder():
    for ext in file_extension:
        each_folder = Path(f"{organised}/{ext}_file")
        each_folder.mkdir(exist_ok=True)





# Store files in respective folder
def sort_file(folder_name):
    for ext in file_extension: 
        for file in folder_name.glob(f"*{ext}"):
            source = f"{folder_name}/{file.name}"
            destination = f"{organised}/{ext}_file/{file.name}"
            shutil.move(source, destination)




# things to work on: update your code to allow it to access files inside folders in folders