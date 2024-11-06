import os
import shutil
folder_path=input('csv파일들이 있는 폴더의 경로를 입력하시오:') # 탐색할 폴더의 경로
if not os.path.isdir(folder_path):  #  폴더의 위치 확인
    print("올바른 폴더 경로가 아닙니다. 다시 시도하세요:")
    exit()

    
search_phrase="checked_files_"
def change_name(root, file):
    # 파일 이름을 'checked_files_'로 시작하도록 변경하는 함수"
    old_file_path = os.path.join(root, file) # 주어진 디렉토리에서 파일의 전체 경로 생성
    new_file_name = f"checked_files_{file}"  # 파일 이름을 새로 지정할 때 원래 파일이름에 'checked_files_' 붙이기
    new_file_path = os.path.join(root, new_file_name)   #새로운 파일의 경로
    os.rename(old_file_path, new_file_path)  
    print(f"Renamed: {new_file_name}, New Path: {new_file_path}")



def check_word_in_file(file_path, phrase):
    """파일 이름에 특정 구문이 포함되지 않은 경우 이름을 변경하는 함수"""
    for root, dirs, files in os.walk(file_path):   
        for file in files:
            if file.endswith('.csv') and phrase not in file: # 만약에 파일 종류 CSV파일이고 PHRASE 가 파일 안에 없다면 change_name한다
                change_name(root, file)
            
       
                
if __name__=="main":
    check_word_in_file(folder_path, search_phrase)
else:
    print("모듈이 import 되있다")
