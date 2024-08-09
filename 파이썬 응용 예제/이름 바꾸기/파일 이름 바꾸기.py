import os
import pandas as pd
import shutil
import logging
logging.debug("info log")
folder_path='C:/Users/kim/P_Ver1/P_2/data'
search_phrase="checked_files_"

def change_name():
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                old_file_path=os.path.join(root,file)
                new_file_name=f"checked_files_{file}"
                new_file_path= os.path.join(root,new_file_name) 
                os.rename(old_file_path,new_file_path)
                print(f"{new_file_name},,,,,,,{new_file_path}")

# def find_files_phrase(folder_path,phrase):
#     piles= os.listdir(folder_path)
#     matching_files=[]
#     for pile in piles:
#         if phrase in pile:
#             matching_files.append(pile) 
#     return matching_files
# matching_files=find_files_phrase(folder_path,phrase)

# if matching_files:
#     for pile in matching_files:
found=True
def check_word_in_file(file_path,phrase):
    for root, dir,files in os.walk(file_path):
        for pile in files:
            if not phrase in pile:
                change_name() 
                break
        if found:
            break
            
       
                
    
check_word_in_file('C:/Users/kim/P_Ver1/P_2/data',search_phrase)
