import pandas as pd 
import os
import subprocess
def count_nan_rows_in_multiple_columns(root_folder, column_prefix, column_range, chunk_size=10000):
    nan_row_count = 0
    transition_count = 0

    # 열 이름 리스트 생성 (예: ['cell_b1', 'cell_b2', ..., 'cell_b180'])
    columns = [f"{column_prefix}{i}" for i in range(1, column_range + 1)]

    # 폴더 내부의 모든 파일과 하위 폴더 탐색
    for folder_path, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # 파일이 CSV 파일인지 확인
            if filename.lower().endswith('.csv'):
                full_path = os.path.join(folder_path, filename)
                print(f"Processing file: {full_path}")

                try:
                    # 이전 청크의 마지막 행을 저장하기 위한 변수 초기화
                    previous_chunk_last_row = None
                    # 청크 단위로 CSV 파일 읽기 (지정된 열만 불러옴)
                    for chunk in pd.read_csv(full_path, usecols=columns, chunksize=chunk_size):
                        # 모든 지정된 열에서 결측치가 있는 행을 찾음
                        nan_row_count += chunk[chunk[columns].isna().any(axis=1)].shape[0]
                    # 열별로 전 행이 0이 아닌데 다음 행에서 0이 나오는 경우 찾기
                        if previous_chunk_last_row is not None:
                            # 이전 청크의 마지막 행과 현재 청크의 첫 번째 행 비교
                            transition_count += ((previous_chunk_last_row != 0) & (chunk.iloc[0] == 0)).sum()
                        # 현재 청크 내부에서의 연속성 검사
                        transition_count += ((chunk.shift(1) != 0) & (chunk == 0)).sum().sum()
 
                        # 현재 청크의 마지막 행 저장
                        previous_chunk_last_row = chunk.iloc[-1]

                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    print(f"Total rows with error {nan_row_count+transition_count}")
    return nan_row_count, transition_count

# 사용 예시
root_folder = '' # 폴더 경로 지정
column_prefix = ''  # 열 이름의 접두사
column_range =   # 열의 수
