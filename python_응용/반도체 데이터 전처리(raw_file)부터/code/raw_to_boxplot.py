

import os
import pandas as pd
import matplotlib.pyplot as plt

def boxplot_for_all_columns(file_path, x_column, output_folder):
    # 결과 이미지 파일을 저장할 폴더가 존재하지 않으면 생성
    os.makedirs(output_folder, exist_ok=True)
    
    # CSV 파일 읽기
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return
    
    # x_column을 datetime 형식으로 변환 (필요한 경우)
    if x_column in df.columns:
        df[x_column] = pd.to_datetime(df[x_column], errors='coerce')
    else:
        print(f"Column '{x_column}' not found in the DataFrame.")
        return
    
    # 결측치 확인 및 제거
    df_cleaned = df.dropna(subset=[x_column])
    if df_cleaned.empty:
        print(f"No data available after removing missing values in {x_column}.")
        return
    
    # x_column을 제외한 나머지 모든 열을 y_columns로 설정
    y_columns = [col for col in df.columns if col != x_column]
    
    # 각 y 열에 대해 산점도 생성
    for y_column in y_columns:
        # 결측치가 있는 경우 해당 데이터 제거
        df_y_cleaned = df_cleaned.dropna(subset=[y_column])
        
        if df_y_cleaned.empty:
            print(f"No data available for {y_column} after removing missing values.")
            continue
        
        # Boxplot 생성
        plt.figure(figsize=(8, 6))
        plt.boxplot(df_y_cleaned[y_column])
        plt.title(f'Boxplot of {y_column}')
        plt.xlabel(y_column)
        plt.grid(True)
        
        # 이미지 파일로 저장
        output_image_path = os.path.join(output_folder, f'{y_column}_boxplot.png')
        plt.savefig(output_image_path)
        plt.close()
        print(f"boxplot saved: {output_image_path}")

# 예제 CSV 파일 경로
file_path = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/data_merge.csv'

# 결과 이미지 파일을 저장할 폴더 경로
output_folder = '/mnt/c/Users/kim/P_Ver1/data_semicoductor/raw_data/시각 자료/boxplot/'

# 데이터 생성 및 저장
boxplot_for_all_columns(file_path, 'TIME', output_folder)