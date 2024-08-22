import os
import pandas as pd
import shutil
import logging
logging.debug("info log")
folder_path='C:/Users/kim/P_Ver1/P_2/data' # 탐색할 폴더의 경로
search_phrase="checked_files_"

def change_name():
    # 루트 경로로 부터 하위 디렉토리 및 파일들 탐색
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            #파일 형식이 csv이면, 
            if file.endswith('.csv'):
                old_file_path=os.path.join(root,file) #현재 파일의 기존 경로 생성
                new_file_name=f"checked_files_{file}" # 새로운 파일 이름 생성할 때 기존파일 앞에 'checked_files_' 추가
                new_file_path= os.path.join(root,new_file_name)  #새 파일 경로 생성
                os.rename(old_file_path,new_file_path)  #기존 파일을 새 파일 이름으로 변경
                print(f"{new_file_name},,,,,,,{new_file_path}")



found=True
def check_word_in_file(file_path,phrase):
    for root, dir,files in os.walk(file_path): # 만약 file_path 디렉토리를 시작으로 하위 디렉토리까지 순회 했을 때
        for pile in files:  
            if not phrase in pile: #pile 안에 phrase가 없을 시 이름을 바꿈
                change_name() 
                break #반복문 끝내기
        if found:  # 안에 phrase가 있을시 반복문 끝내기
            break
            
       
                
    
check_word_in_file('C:/Users/kim/P_Ver1/P_2/data',search_phrase)
