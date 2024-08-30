import pandas as pd
import os

def read_and_process_file(file_path):
    ###CSV 파일을 읽고, 영문 파일명과 TIME, STEP, STEP_NAME, VALUE 데이터를 반환
    df = pd.read_csv(file_path)
    # 파일명에서 영문 부분 추출
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # 필요한 열만 추출
    df = df[['TIME', 'VALUE']]
    # 열 이름 변경
    df.rename(columns={'VALUE': file_name}, inplace=True)
    return df

def merge_csv_files(folder_path, output_file):
    ##폴더 내 모든 CSV 파일을 병합하고, TIME 기준으로 정렬하여 하나의 CSV 파일로 저장
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # 모든 CSV 파일에서 데이터 읽어오기
    dataframes = []
    
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = read_and_process_file(file_path)
        dataframes.append(df)
    
    # TIME을 기준으로 병합
    merged_df = dataframes[0]
    
    for df in dataframes[1:]:
        merged_df = pd.merge(merged_df, df, on=['TIME'], how='outer', suffixes=('', '_dup'))
    
    # 중복된 열 처리
    # 동일한 열을 하나로 병합
    for col in merged_df.columns:
        if col.endswith('_dup'):
            original_col = col.replace('_dup', '')
            if original_col in merged_df.columns:
                merged_df[original_col] = merged_df[[original_col, col]].bfill(axis=1).iloc[:, 0]
                merged_df.drop(columns=[col], inplace=True)

    # TIME 기준으로 정렬
    merged_df.sort_values(by='TIME', inplace=True)

    #사용자 지정 헤더
    user_defined_header=['TIME','GAS_DCS','GAS_F2','GAS_N2_1','GAS_N2_2','GAS_N2_3','GAS_N2_4','GAS_N2_LOADING_AREA','GAS_N2_NR','GAS_NH3','PRESSURE_APC_ANGLE','PRESSURE_VG1','PRESSURE_VG2','TEMP_PROFILE_1','TEMP_PROFILE_2','TEMP_PROFILE_3','TEMP_PROFILE_4','TEMP_PROFILE_5']
    
    if len(user_defined_header) != len(merged_df.columns):
        print("사용자 지정 헤더 길이가 데이터프레임의 열수와 맞지 않음")
    else:
        merged_df.columns =user_defined_header
    # 최종 CSV 파일로 저장
    merged_df.to_csv(output_file, index=False)


folder_path = './data'  # CSV 파일이 위치한 폴더 경로
output_file = 'semi_data.csv'  # 출력할 파일명(.csv붙여야 함)
if __name__='__main__':
    merge_csv_files(folder_path, output_file)
