import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_and_save_histograms(file_path, output_folder, columns):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    
    # 출력 폴더가 존재하지 않으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# 각 변수에 대해 히스토그램 생성
    for column in related_columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df[column].dropna(), bins=30, alpha=0.7, color='blue', edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
# 이를 png파일로 저장 후 output_file에 저장
        output_file = os.path.join(output_folder, f'{column}_histogram.png')
        plt.savefig(output_file)
        plt.close()

file_path='./data/GAS_NH3_(S등급)_Sheet1-Copy1.csv'
output_folder='./histogram'
related_columns =['VALUE']

plot_and_save_histograms(file_path, output_folder, related_columns)
