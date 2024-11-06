import pandas as pd
import os
import time

def divide_large_file_to_small_files(root_folder_path, output_folder_path):   
    # 시작 시간 기록
    start_time = time.time()
    
    # 출력 폴더가 존재하지 않으면 생성
    os.makedirs(output_folder_path, exist_ok=True)
    csv_files = []
    
    # 폴더 내부의 모든 CSV 파일 탐색
    for folder_path, subfolders, filenames in os.walk(root_folder_path):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                full_path = os.path.join(folder_path, filename)
                csv_files.append(full_path)
    
    # 각 CSV 파일에 대해 새로운 폴더 생성 및 파일 나누기
    for file_path in csv_files:
        # 원본 파일의 폴더 경로에서 root_folder_path 부분을 제거하여 상대 경로 생성
        relative_folder = os.path.relpath(os.path.dirname(file_path), root_folder_path)
        # output_folder_path에 상대 경로를 추가하여 새로운 폴더 경로 생성
        new_folder_path = os.path.join(output_folder_path, relative_folder, os.path.basename(file_path).replace('.csv', ''))
        # 새로운 폴더가 존재하지 않으면 생성
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"폴더 생성 완료: {new_folder_path}")
        else:
            print(f"폴더가 이미 존재합니다: {new_folder_path}")
        
        # CSV 파일 읽기 및 나누기
        try:
            # Chunk 단위로 CSV 파일 읽기
            chunk_size = 50000
            chunk_number = 1
            name = os.path.basename(file_path).replace('.csv', '')
            
            # 열 이름을 대문자로 변환할 리스트
            columns_to_include_upper = [col.upper() for col in columns_to_include]

            for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
                # 데이터 프레임의 열 이름을 대문자로 변환하여 비교
                chunk.columns = chunk.columns.str.upper()
                chunk = chunk[[col for col in chunk.columns if col in columns_to_include_upper]]
                # 특정 B_CELL{i}_VOLT 열에 대해서만 비교 연산 수행
                cell_columns = [f"B_CELL{i}_VOLT" for i in range(1, 181) if f"B_CELL{i}_VOLT" in chunk.columns]
                numeric_chunk = chunk[cell_columns]

                # 결측치가 있거나 0~0.4 사이의 값을 포함하는 행을 제외
                condition = ~((numeric_chunk.isna().any(axis=1)) | ((numeric_chunk >= 0) & (numeric_chunk <= 0.4)).any(axis=1))
                filtered_chunk = chunk[condition]
                
                chunk_file_name = f"{name}_part_{chunk_number}.csv"
                chunk_file_path = os.path.join(new_folder_path, chunk_file_name)
                
                # 분할된 파일 저장
                filtered_chunk.to_csv(chunk_file_path, index=False)
                print(f"파일 저장 완료: {chunk_file_path}")
                
                chunk_number += 1
                
        except Exception as e:
            print(f"파일 처리 중 오류 발생: {e}")

    # 종료 시간 기록 및 걸린 시간 계산
    end_time = time.time()
    total_time = end_time - start_time
    print(f"총 걸린 시간: {total_time // 3600}시간 {total_time % 3600 // 60}분 {total_time % 60}초")

# 경로 설정
root_folder_path = '/mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/divided_sk_car'
output_folder_path = '/mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/preprocessing'
columns_to_include=[
'DEV_ID','COLL_DT','B_SOC','B_SOH','B_PACK_CURRENT','B_PACK_VOLT','B_MAX_TEMP','B_SLOW_CHARG_CON_STS','B_FAST_CHARG_CON_STS',*[f"B_CELL{i}_VOLT" for i in range(1,181)]
]

divide_large_file_to_small_files(root_folder_path, output_folder_path)
