
import pandas as pd
import matplotlib.pyplot as plt
import os  

def plot_step_overlay(file_path, x_column, output_image_path):
    # 결과 이미지를 저장할 디렉토리 생성
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    
    # TIME 열을 datetime 형식으로 변환 (필요한 경우)
    df[x_column] = pd.to_datetime(df[x_column])
    
    # x 열을 제외한 모든 열을 y값으로 사용
    y_columns = df.columns.difference([x_column])
    
    # 단계 플롯 생성
    plt.figure(figsize=(12, 6))
    
    # 각 y 열에 대해 단계 플롯 추가
    for y_column in y_columns:
        # 결측치 있는 행 제거
        df_cleaned = df.dropna(subset=[x_column, y_column])
        
        if df_cleaned.empty:
            print(f"No data available for {y_column} after removing missing values.")
            continue
        
        plt.step(df_cleaned[x_column], df_cleaned[y_column], where='post', label=y_column)

        # 결측치 수 출력
        missing_y = df[y_column].isna().sum()
        print(f"Missing values in {y_column}: {missing_y}")
    
    plt.title(f'All Data vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
        
        # 이미지 파일로 저장
    output_image_path = os.path.join(output_folder, f'{y_column}_boxplot.png')
    plt.savefig(output_image_path)
    plt.close()
    print(f"stepplot saved: {output_image_path}")

# 예제 CSV 파일 경로
file_path = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_merge.csv'

# 결과 이미지 파일을 저장할 폴더 경로
output_folder = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/시각 자료/전체/계단형/'

# 데이터 생성 및 저장
plot_step_overlay(file_path, 'TIME', output_folder)