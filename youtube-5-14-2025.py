import os

folder_path = "C:/Users/ALAMEEN/Documents/New folder"

new_name = "DOC_"

count = 1

files = os.listdir(folder_path)

for file in files:
    
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1]
        new_file_name = f"{new_name}{count:03}{ext}"
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file} -- {new_file_name}")
        count += 1