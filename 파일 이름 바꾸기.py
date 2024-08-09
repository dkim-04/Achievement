import os

import pandas as pd

folder_path='C:/Users/kim/P_Ver1/P_2/data'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.csv'):
            old_file_path=os.path.join(root,file)
            new_file_name=f"checked_files_{file}"
            new_file_path= os.path.join(root,new_file_name) 
            os.rename(old_file_path,new_file_path)
            print(f"{new_file_name},,,,,,,{new_file_path}")