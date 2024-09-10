




## 전체 파일을 csv로 변환후 하나의 파일로 통합하는 코드
import os
import pandas as pd 

def change_xlsx_and_move_csv(root_folder_path,target_folder_path):
    os.makedirs(target_folder_path,exist_ok=True)
    # 모든 하위 폴더 포함해 파일 검색
    for folder_path, subfolders, filenames in os.walk(root_folder_path):
        for filename in filenames:
            # 파일이 엑셀 파일(.xlsx)인지 확인
            if filename.lower().endswith(".xlsx" ):
                # 엑셀 파일의 전체 경로를 구성
                excel_file_path = os.path.join(folder_path, filename)
                try:
                # 엑셀 파일을 읽어옵니다.
                    df = pd.read_excel(excel_file_path)
                
                # 동일한 이름의 CSV 파일로 저장할 경로를 설정
                    csv_filename = filename.replace('.xlsx', '.csv')
                    csv_file_path = os.path.join(target_folder_path, csv_filename)
                    # DataFrame을 CSV 파일로 저장합니다.
                    df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
                except Exception as e:
                    print(f"Error processing file{excel_file_path}:{e}")


def read_and_process_file(file_path):
    ###CSV 파일을 읽고, 영문 파일명과 TIME, VALUE 데이터를 반환
    df = pd.read_csv(file_path)
    # 파일명에서 영문 부분 추출
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    if 'TIME' not in df.columns or 'VALUE' not in df.columns:
        print(f"Skipping {file_path}: Required columns are missing")
        return None
        
    # 필요한 열만 추출
    df = df[['TIME', 'VALUE']]
    # 열 이름 변경
    df.rename(columns={'VALUE': file_name}, inplace=True)
    df_cleaned=df.drop_duplicates(subset=['TIME'])
    return df_cleaned
   
def merge_csv_files(folder_path,output_file):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    # 모든 csv파일에서 데이터 읽어오기
    dataframes =[]
    for file in csv_files:
        file_path = os.path.join(folder_path,file)
        df = read_and_process_file(file_path)
        dataframes.append(df)
    if not dataframes:
        print("No valid dataframes to merge.")
        return
    # Time 기준 병합
    merged_df = dataframes[0]

    for df in dataframes[1:]:
        merged_df=pd.merge(merged_df,df,on=['TIME'],how='outer',suffixes=('','_dup'))

    #중복된 열 처리
    # 동일한 열을 하나로 병합
    #결측치 처리
    for col in merged_df.columns:
        if  col.endswith('_dup'):
            original_col=col.replace('_dup','') #original_col=원본열,col= 중복열
            if original_col in merged_df.columns:
                merged_df[original_col] = merged_df[[original_col,col]].bfill(axis=1).iloc[:,0]   # axis=1 행이 아닌 열 기준으로 결측치 채우도록 지시 iloc= Dataframe의 행과 열을 위치 기반으로 선택
                merged_df.drop(columns=[col],inplace=True)

        
     # 결측치 제거
    merged_df.dropna(inplace=True)
    # TIME 기준으로 정렬
    merged_df.sort_values(by='TIME', inplace=True)

    #최종 csv파일로 저장
    merged_df.to_csv(output_file, index=False)
    

folder_path='/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_csv_Ver'
output_file='/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_merge.csv'
        
                

if __name__=="__main__":
    root_folder_path='/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data'
    target_folder_path='/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_csv_Ver'
    change_xlsx_and_move_csv(root_folder_path,target_folder_path)
    merge_csv_files(folder_path,output_file)
