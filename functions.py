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

        # check for file_extensions inside folder
        elif file.is_dir():
            get_file_extension(file)
    


# Create folder to store files
def create_storage_folder():
    for ext in file_extension:
        each_folder = Path(f"{organised}/{ext}_file")
        each_folder.mkdir(exist_ok=True)


def move_file(file, ext):
    source = f"{file.parent}/{file.name}"
    destination = f"{organised}/{ext}_file/{file.name}"
    shutil.move(source, destination)



# Store files in respective folder
def sort_file(folder_name):
    for ext in file_extension: 
        for file in folder_name.iterdir():
            if file.is_file():
                for file in folder_name.glob(f"*{ext}"):
                   move_file(file, ext)


            # To check for files in folder inside folder
            elif file.is_dir():
                for f in file.glob(f"*{ext}"):
                   move_file(f, ext)





        # for file in folder_name.glob(f"*{ext}"):
        #     source = f"{file.parent}/{file.name}"
        #     print(source)
        #     print(file.parent)
        #     destination = f"{organised}/{ext}_file/{file.name}"
        #     shutil.move(source, destination)




# things to work on: update your code to allow it to access files inside folders in folders