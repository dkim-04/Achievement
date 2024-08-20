#### 다른 기기에서 실행할 때 결과 이미지 파일 경로 및 예제 csv파일 수정 필요
####
###  이 코드가 작동하려면 semi_data파일이 필요함
###
###


import pandas as pd
import matplotlib.pyplot as plt

def plot_scatter_overlay(file_path, x_column, y_columns, output_image_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    
    # TIME 열을 datetime 형식으로 변환 (필요한 경우)
    df[x_column] = pd.to_datetime(df[x_column])
    
    # 산점도 생성
    plt.figure(figsize=(12, 6))
    
    # 각 y 열에 대해 산점도 추가
    for y_column in y_columns:
        plt.scatter(df[x_column], df[y_column], alpha=0.7, label=y_column, edgecolors='k')

        # 결측치 확인 및 처리
        missing_y = df[y_column].isna().sum()
        print(f"Missing values in {y_column}: {missing_y}")
        
        # 결측치가 있는 경우 해당 데이터 제거
        df_cleaned = df.dropna(subset=[x_column, y_column])
        
        if df_cleaned.empty:
            print(f"No data available for {y_column} after removing missing values.")
            continue
        
        # x와 y 데이터 길이 확인
        if len(df_cleaned[x_column]) != len(df_cleaned[y_column]):
            print(f"Length mismatch between {x_column} and {y_column}.")
            continue
    
    plt.title(f' ALL_data VS {x_column}')
    plt.xlabel(x_column)
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    
    # 이미지 파일로 저장
    plt.savefig(output_image_path)
    plt.show()

# 예제 CSV 파일 경로
file_path = 'semi_data2.csv'

# y축으로 사용할 열 몰록
y_columns = ['GAS_DCS', 'GAS_F2', 'GAS_N2_1', 'GAS_N2_2', 'GAS_N2_3', 'GAS_N2_4', 'GAS_N2_LOADING_AREA', 'GAS_N2_NR', 'GAS_NH3', 'PRESSURE_APC_ANGLE', 'PRESSURE_VG1', 'PRESSURE_VG2', 'TEMP_PROFILE_1', 'TEMP_PROFILE_2', 'TEMP_PROFILE_3', 'TEMP_PROFILE_4', 'TEMP_PROFILE_5']  
# 결과 이미지 파일 경로
output_image_path = './산점도_data/ALL/전체_산점도.png'

# 산점도 생성 및 저장
plot_scatter_overlay(file_path, 'TIME', y_columns, output_image_path)
