import os
import shutil
folder_path=input('csv파일들이 있는 폴더의 경로를 입력하시오:') # 탐색할 폴더의 경로
if not os.path.isdir(folder_path):
    print("올바른 폴더 경로가 아닙니다. 다시 시도하세요:")
    exit()

    
search_phrase="checked_files_"
def change_name(root, file):
    """파일 이름을 'checked_files_'로 시작하도록 변경하는 함수"""
    old_file_path = os.path.join(root, file)
    new_file_name = f"checked_files_{file}"
    new_file_path = os.path.join(root, new_file_name)
    os.rename(old_file_path, new_file_path)
    print(f"Renamed: {new_file_name}, New Path: {new_file_path}")



def check_word_in_file(file_path, phrase):
    """파일 이름에 특정 구문이 포함되지 않은 경우 이름을 변경하는 함수"""
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.csv') and phrase not in file:
                change_name(root, file)
            
       
                
    
check_word_in_file(folder_path, search_phrase)
