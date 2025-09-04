import os
import shutil

def create_subfolder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder(folder_path, subfolder_name)
                dest_path = os.path.join(subfolder_path, filename)
                if os.path.exists(dest_path):
                    print(f"Skipped: {filename} (destination already exists)")
                else:
                    shutil.move(file_path, subfolder_path)
                    print(f'Moved: {filename} to {subfolder_name}')

            


if __name__ == "__main__":
    print("Desktop Cleaner")
    folder_path = '/Users/grantsuchecki/Downloads'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print('Cleaning Complete!')
    else:
        print('Invalid folder path! Please ensure the path is correct and try again.')