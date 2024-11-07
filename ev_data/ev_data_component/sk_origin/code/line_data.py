import pandas as pd 
import os
import gc  # 가비지 컬렉션을 위해 추가
import time  # 시간 측정을 위해 추가

def count_nan_rows_in_multiple_columns_before(root_folder, column_prefix, column_suffix, column_range, chunk_size=10000):
    start_time = time.time()
    combined_count = 0
    total_rows = 0

    # 열 이름 리스트 생성
    columns_lower = ["{0}{1}_{2}".format(column_prefix.lower(), i, column_suffix.lower()) for i in range(1, column_range + 1)]
    columns_upper = ["{0}{1}_{2}".format(column_prefix.upper(), i, column_suffix.upper()) for i in range(1, column_range + 1)]
    columns = columns_lower + columns_upper

    for folder_path, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                full_path = os.path.join(folder_path, filename)
                print(f"Processing file: {full_path}")

                try:
                    for chunk in pd.read_csv(full_path, usecols=lambda col: col.lower() in [col.lower() for col in columns], chunksize=chunk_size):
                        if chunk.empty:
                            print(f"Warning: Empty chunk in file {full_path}")
                            continue
                        
                        total_rows += len(chunk)
                        chunk = chunk.astype('float32')

                        # 결측치가 있거나, 0~0.4 사이인 값을 포함한 행만 필터링하여 카운트
                        combined_count += chunk[(chunk.isna().any(axis=1)) | ((chunk >= 0) & (chunk <= 0.4)).any(axis=1)].shape[0]

                        # 메모리 관리
                        del chunk
                        gc.collect()
                        
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    total_time = time.time() - start_time
    print(f"Total rows before preprocess: {total_rows}") 
    print(f"Total rows with issues before preprocess: {combined_count}")
    print(f"Total time taken before preprocess: {total_time:.2f} seconds")
    return combined_count, total_time, total_rows

def count_nan_rows_in_multiple_columns_after(root_folder, column_prefix, column_suffix, column_range, chunk_size=10000):
    start_time = time.time()
    combined_count = 0
    total_rows = 0

    # 열 이름 리스트 생성
    columns_lower = ["{0}{1}_{2}".format(column_prefix.lower(), i, column_suffix.lower()) for i in range(1, column_range + 1)]
    columns_upper = ["{0}{1}_{2}".format(column_prefix.upper(), i, column_suffix.upper()) for i in range(1, column_range + 1)]
    columns = columns_lower + columns_upper

    for folder_path, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                full_path = os.path.join(folder_path, filename)
                print(f"Processing file: {full_path}")

                try:
                    for chunk in pd.read_csv(full_path, usecols=lambda col: col.lower() in [col.lower() for col in columns], chunksize=chunk_size):
                        if chunk.empty:
                            print(f"Warning: Empty chunk in file {full_path}")
                            continue
                        
                        total_rows += len(chunk)
                        chunk = chunk.astype('float32')

                        # 결측치가 있거나, 0~0.4 사이인 값을 포함한 행만 필터링하여 카운트
                        combined_count += chunk[(chunk.isna().any(axis=1)) | ((chunk >= 0) & (chunk <= 0.4)).any(axis=1)].shape[0]

                        # 메모리 관리
                        del chunk
                        gc.collect()
                        
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    total_time = time.time() - start_time
    print(f"Total row after preprocess: {total_rows}") 
    print(f"Total rows with issues after preprocess: {combined_count}")
    print(f"Total time taken after preprocess: {total_time:.2f} seconds")
    return combined_count, total_time, total_rows

# 사용 예시
root_folder = '/mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/divided_sk_car'  # 폴더 경로 지정
column_prefix = 'B_CELL'  # 열 이름의 접두사
column_suffix = 'VOLT'  # 열 이름의 접미사
column_range = 180  # 열의 수
after_folder='/mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/preprocessing'
if __name__=="__main__":
    count_nan_rows_in_multiple_columns_before(root_folder, column_prefix, column_suffix, column_range)
    count_nan_rows_in_multiple_columns_after(after_folder,column_prefix,column_suffix,column_range)
