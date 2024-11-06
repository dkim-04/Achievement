import os
import pandas as pd
import matplotlib.pyplot as plt
import re

# 타임스탬프 형식을 정리하는 함수
def clean_timestamp_format(df, column):
    # 정규 표현식을 이용해 타임스탬프에서 'YYYY-MM-DD HH:MM:SS' 형식만 추출
    df[column] = df[column].apply(lambda x: re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', str(x)).group(0) if pd.notnull(x) else x)
    df[column] = pd.to_datetime(df[column], errors='coerce')  # 추출한 값들로 datetime 변환
    return df

# 진행 상황을 표시하는 Progress Bar 함수
def printProgressBar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

def rate_of_charg(files, output_folder):
    total_files = len(files)

    for i, file_path in enumerate(files):
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue

        # 타임스탬프 형식을 정리 (정규 표현식으로 처리)
        df = clean_timestamp_format(df, 'timestamp')

        # 유효한 데이터 필터링
        df = df.dropna(subset=['timestamp', 'soc', 'soh'])

        # 타임스탬프 정렬
        df = df.sort_values(by='timestamp')

        # 데이터가 없는 경우 건너뛰기
        if df.empty:
            print(f"DataFrame is empty for file: {file_path}")
            continue

        # 파일명에서 확장자를 제거한 파일명 사용
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        relative_path = os.path.relpath(file_path, start=os.path.commonpath(files))
        
        # 하위 폴더 경로를 포함한 출력 폴더 생성
        output_file_folder = os.path.join(output_folder, os.path.dirname(relative_path))
        os.makedirs(output_file_folder, exist_ok=True)  # 하위 폴더 생성
        
        # 차트 그리기
        plt.figure(figsize=(14, 8))
        
        # SOC와 SOH 데이터를 동일한 플롯에 표시
        plt.plot(df['timestamp'], df['soc'], label='SOC', color='blue')
        plt.plot(df['timestamp'], df['soh'], label='SOH', color='green')

        # 첫 번째와 마지막 타임스탬프 값 추출
        first_timestamp = df['timestamp'].iloc[0]
        last_timestamp = df['timestamp'].iloc[-1]
        
        # 첫 번째와 마지막 SOC, SOH 값 추출
        first_soc = df['soc'].iloc[0]
        last_soc = df['soc'].iloc[-1]
        first_soh = df['soh'].iloc[0]
        last_soh = df['soh'].iloc[-1]
        
        # 첫 번째 SOC 값과 타임스탬프를 다른 색으로 표시
        plt.text(first_timestamp, first_soc + 1, f'{first_soc:.2f}', fontsize=12, color='blue', verticalalignment='bottom')
        plt.text(first_timestamp, first_soc - 5, first_timestamp.strftime('%Y-%m-%d %H:%M:%S'), fontsize=10, color='red', verticalalignment='top')

        # 첫 번째 SOH 값과 타임스탬프를 다른 색으로 표시
        plt.text(first_timestamp, first_soh + 1, f'{first_soh:.2f}', fontsize=12, color='green', verticalalignment='bottom')
        

        # 마지막 SOC 값과 타임스탬프를 다른 색으로 표시
        plt.text(last_timestamp, last_soc + 1, f'{last_soc:.2f}', fontsize=12, color='blue', verticalalignment='bottom')
        plt.text(last_timestamp, last_soc - 5, last_timestamp.strftime('%Y-%m-%d %H:%M:%S'), fontsize=10, color='red', verticalalignment='top')

        # 마지막 SOH 값과 타임스탬프를 다른 색으로 표시
        plt.text(last_timestamp, last_soh + 1, f'{last_soh:.2f}', fontsize=12, color='green', verticalalignment='bottom')
       

        # 축 및 제목 설정
        plt.xlabel('Timestamp (HH:MM:SS)')
        plt.ylabel('Values (0-110%)')
        plt.title(f"SOC, SOH over Time - {file_name}")
        plt.legend(loc='upper right')
        plt.grid()

        # 하위 폴더 경로가 포함된 파일 저장 경로 설정
        output_file = os.path.join(output_file_folder, f"rate_of_charge_{file_name}.png")
        plt.savefig(output_file)
        plt.close()

        # 진행 상황 출력
        printProgressBar(i + 1, total_files)

# 디렉토리 내 모든 하위 폴더와 CSV 파일 탐색
def find_all_csv_files(root_folder):
    csv_files = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(dirpath, file))
    return csv_files

# CSV 파일이 저장된 최상위 디렉토리 경로
csv_folder_path = '/mnt/c/Users/kim/P_Ver1/car_data/better_why_data/add_mean/'

# 결과를 저장할 대상 출력 폴더 경로
output_folder = '/mnt/c/Users/kim/P_Ver1/car_data/better_why_data/output_image/rate_of_charg/charge_data/fast_charge_data/'

# 디렉토리 내 모든 CSV 파일 (하위 폴더 포함)
csv_files = find_all_csv_files(csv_folder_path)
rate_of_charg(csv_files, output_folder)
