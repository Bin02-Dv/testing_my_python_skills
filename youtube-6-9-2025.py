import os
import shutil

for file in os.listdir("C:/Users/ALAMEEN/Documents/Documents/my_projects/testing_my_python_skills"):
    if file.endswith(".py"):
        shutil.copy(f"C:/Users/ALAMEEN/Documents/Documents/my_projects/testing_my_python_skills/{file}", f"hacked_copies/{file}")
        print(f"Copied: {file}")