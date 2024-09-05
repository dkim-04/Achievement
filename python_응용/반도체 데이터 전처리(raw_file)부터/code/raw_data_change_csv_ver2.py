## 전체 파일을 csv로 변환후 하나의 파일로 통합하는 코드
import os 
import pandas as pd 

def recursive_search_dir(_nowDir, _filelist, _form):
    """
    현재 디렉토리 및 하위 디렉토리에서 지정된 형식의 파일을 검색하여 목록에 추가하는 함수
    """
    dir_list = []  # 현재 디렉토리의 서브 디렉토리 담길 list
    _nowDir = _nowDir.rstrip('/')  # 디렉토리 경로에서 마지막 '/' 제거
    f_list = os.listdir(_nowDir)  # 현재 디렉토리의 모든 파일 및 디렉토리 목록 가져오기
    
    for fname in f_list:
        full_path = os.path.join(_nowDir, fname)  # 파일의 전체 경로 생성
        if os.path.isdir(full_path):  # 만약 현재 경로가 디렉토리라면
            dir_list.append(full_path)
        elif os.path.isfile(full_path):  # 만약 현재 경로가 파일이라면
            file_extension = os.path.splitext(fname)[1]
            if file_extension.lower() == '.' + _form.lower():  # 확장자가 지정한 형식과 일치할 때
                _filelist.append(full_path)

    for toDir in dir_list:  # 서브 디렉토리들에 대해 재귀적으로 탐색
        recursive_search_dir(toDir, _filelist, _form)


def excel_to_csv(excel_file, save_path):
    """
    Excel 파일의 모든 시트를 개별 CSV 파일로 저장하는 함수
    """
    # EXCEL 파일 읽기
    d = pd.read_excel(excel_file, engine='openpyxl', sheet_name=None)
    
    # save_path에 dir가 존재하지 않으면 디렉토리 생성
    os.makedirs(save_path, exist_ok=True)
    
    # 각 시트를 순환하면서 CSV 파일로 저장
    for sheet_name, df in d.items():
        # CSV 파일로 저장
        csv_file_name = os.path.join(
            save_path, 
            f"{os.path.splitext(os.path.basename(excel_file))[0]}_{sheet_name}.csv"
        )
        df.to_csv(csv_file_name, index=False, encoding='utf-8-sig')  # 인코딩을 UTF-8-SIG로 설정
        print(f'{csv_file_name} 파일이 UTF-8-SIG 인코딩으로 저장되었습니다.')


# Excel 파일 경로를 저장할 리스트 초기화
excel_list = []

# Excel 파일이 있는 디렉토리 설정
excel_data_path = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data'

# 지정된 디렉토리에서 모든 Excel 파일 찾기
recursive_search_dir(excel_data_path, excel_list, 'xlsx')

# CSV 파일을 저장할 경로
save_path = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_csv_Ver/'

# 찾은 모든 Excel 파일을 CSV로 변환하여 저장
for excel_file in excel_list:
    excel_to_csv(excel_file, save_path)



  
                

    
