import time
import sys
import os
import pandas as pd
import csv
import shutil



def printProgressBar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=50, fill='█'):
   
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))) ##반복
    filledLength = int(length * iteration // total) ## 전체 과정 반복 중 progressbar가 얼마나 차야 하는지를 보여주는 역할
    bar = fill * filledLength + '-' * (length - filledLength) #█*filledLength + /"-"*(전체 length-채워져 있는 영역)=█*filledLength ////"-"* 안채워져 있는 부분
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    sys.stdout.flush() ## print() 함수의 개행 여부와 상관 없이 출력 해주는 기능

    if iteration == total:
        print()


def copy_files_with_phrase(folder_path,destination_folder,search_phrase):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    try:
        files=os.listdir(folder_path)
        
        csv_files=[f for f in os.listdir(folder_path) if f.lower().endswith('.csv') and search_phrase in f.lower()] #특정 폴더 내 파일 목록에서 csv파일 만을 필터링
        #특정 단어가 포함된 파일만을 선택


        if csv_files:
            print(f"총 {len(csv_files)}개의 파일이 발견되었습니다:")

            for filename in csv_files:
                src_path=os.path.join(folder_path,filename)
                dst_path=os.path.join(destination_folder,filename)
                
                
                try:
                    shutil.copy(src_path,dst_path)
                    print(f"파일 복사됨:{filename}->{dst_path}")
                except Exception as e:
                    print(f"\n파일 복사 실패: {filename}. 오류: {e}")
        else:
            print("특정 단어가 포함된 csv파일 존재 X")

    except FileNotFoundError:
        print(f"지정된 folder_path가 존재 하지 않는다")
    except Exception as e:
        print(f"오류 발생:{e}")

                
        


folder_path='/mnt/c/Users/kim/P_Ver1/P_2/data'
destination_folder = '/mnt/c/Users/kim/P_Ver1/P_2/processed'
search_phrase='checked_files_'

copy_files_with_phrase(folder_path,destination_folder,search_phrase)



