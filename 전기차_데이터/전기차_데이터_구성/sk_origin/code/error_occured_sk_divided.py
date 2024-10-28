import pandas as pd 
import os
import gc  # 가비지 컬렉션을 위해 추가
import time  # 시간 측정을 위해 추가
import paramiko

def connect_to_server(host, port, username, password):
    """원격 서버에 SSH 연결"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    return ssh

def read_remote_csv(ssh, remote_path, columns, chunk_size):
    """원격 서버에서 CSV 파일을 청크 단위로 읽어오기"""
    sftp = ssh.open_sftp()
    try:
        with sftp.open(remote_path, 'r') as remote_file:
            while True:
                chunk = pd.read_csv(remote_file, usecols=columns, chunksize=chunk_size)
                if chunk.empty:
                    break
                yield chunk.astype('float32')
    finally:
        sftp.close()

def count_nan_rows_in_multiple_columns_on_remote(host, port, username, password, root_folder, column_prefix, column_suffix, column_range, chunk_size=10000):
    start_time = time.time()
    combined_count = 0

    # SSH 서버 연결
    ssh = connect_to_server(host, port, username, password)
    try:
    ssh.exec_command('echo Connection Successful')
    except Exception as e:
    print(f"SSH connection test failed: {e}")
    # 열 이름 리스트 생성
    columns_lower = [f"{column_prefix.lower()}{i}_{column_suffix.lower()}" for i in range(1, column_range + 1)]
    columns_upper = [f"{column_prefix.upper()}{i}_{column_suffix.upper()}" for i in range(1, column_range + 1)]
    columns = columns_lower + columns_upper

    # 원격 디렉토리 파일 탐색
    stdin, stdout, stderr = ssh.exec_command(f'find {root_folder} -name "*.csv"')
    filenames = stdout.read().decode().splitlines()

    for remote_path in filenames:
        print(f"Processing file: {remote_path}")
        try:
            previous_chunk_last_row = None
            for chunk in read_remote_csv(ssh, remote_path, columns, chunk_size):
                if chunk.empty:
                    print(f"Warning: Empty chunk in file {remote_path}")
                    continue

                # 결측치가 있거나, 0~0.4 사이인 값을 포함한 행만 필터링하여 카운트
                combined_count += chunk[(chunk.isna().any(axis=1)) | ((chunk >= 0) & (chunk <= 0.4)).any(axis=1)].shape[0]

                if previous_chunk_last_row is None:
                    # 결측치일 경우 다음 행이 0~0.4인지 확인
                    if ((chunk.iloc[0] >= 0) & (chunk.iloc[0] <= 0.4)).any():
                        combined_count += 1
                else:
                    # 결측치가 없을 때는 이전과 동일하게 처리
                    combined_count += ((previous_chunk_last_row > 1.5) & (chunk.iloc[0] >= 0) & (chunk.iloc[0] <= 0.4)).sum()
                
                # 현재 청크 내부에서의 연속성 검사
                combined_count += (((chunk.shift(1) > 1.5) & (chunk >= 0) & (chunk <= 0.4)).sum().sum())
                
                if not chunk.iloc[-1].isna().any():
                    previous_chunk_last_row = chunk.iloc[-1]
                else:
                    previous_chunk_last_row = None

                del chunk
                gc.collect()
        except Exception as e:
            print(f"Error reading {remote_path}: {e}")

    ssh.close()
    total_time = time.time() - start_time
    print(f"Total rows with issues: {combined_count}")
    print(f"Total time taken: {total_time:.2f} seconds")
    return combined_count, total_time

host = input('서버 ip를 입력하시오')
port = input('서버 포트를 입력하시오')  # 서버 포트 번호
username = input('서버 user_name을 입력하시오')
password = input('서버 비밀번호를 입력하시오')
# 폴더 위치
root_folder = '/mnt/disk/disk02/divided_sk_car'  # 폴더 경로 지정
column_prefix = 'B_CELL'  # 열 이름의 접두사
column_suffix = 'VOLT'  # 열 이름의 접미사
column_range = 180  # 열의 수
count_nan_rows_in_multiple_columns_on_remote(host, port, username, password, root_folder, column_prefix, column_suffix, column_range)
