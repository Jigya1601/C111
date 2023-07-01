import os
import shutil

from_dir = "C:/Users/admin/Downloads"
to_dir = "C:/Users/admin/OneDrive/Desktop/Downloaded_files"

list_of_files = os.listdir (from_dir)
print(list_of_files)

for file in list_of_files:
    root,ext = os.path.splitext(file)
    print(root)
    print(ext)