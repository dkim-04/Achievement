import paramiko
import pandas as pd 

def count_lines_on_remote_server(host, username, password, directory):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 원격 서버에 연결
        client.connect(hostname=host, username=username, password=password)

        # CSV 파일의 총 라인 수를 계산하는 명령어
        command = f'find {directory} -type f -name "*.csv" -exec wc -l {{}} + | awk \'{{s+=$1}} END {{print s}}\''
        
        # 명령어 실행
        stdin, stdout, stderr = client.exec_command(command)
        result = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        
        # 에러가 있을 경우 출력
        if error:
            print(f"Error on {host}: {error}")
            return None
        
        print(f"Total lines on {host}: {result}")
        return int(result)
    
    finally:
        client.close()

def count_files_on_remote_server(host, username, password, directory, port=22):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 원격 서버에 연결 (포트 지정)
        client.connect(hostname=host, username=username, password=password, port=port)
        # 폴더 안의 총 파일 갯수 구하는 명령어
        command = f'find {directory} -type f | wc -l'
        # 명령어 실행
        stdin, stdout, stderr = client.exec_command(command)
        result = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        # 에러가 있을 경우 출력
        if error:
            print(f"Error on {host}: {error}")
            return None

        print(f"Total files on {host}: {result}")
        return int(result)

    finally:
        client.close()


def filesamount_on_remote_server(host, username, password, directory, port=22):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 원격 서버에 연결 (포트 지정)
        client.connect(hostname=host, username=username, password=password, port=port)
        # 폴더 용량 구하는 명령어
        command = f'du -sh {directory}'
        # 명령어 실행
        stdin, stdout, stderr = client.exec_command(command)
        result = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        # 에러가 있을 경우 출력
        if error:
            print(f"Error on {host}: {error}")
            return None

        print(f"Total size on {host}: {result}")
        return result

    finally:
        client.close()


# 서버 정보
source_server = {
    "host": "",
    "username": "",
    "password": '',
    "directory": "",
    "port":   # 포트 지정
}

destination_server = {
    "host": "",
    "username": "",
    "password": "",
    "directory": "",
    "port":   # 포트 지정
}
# 서버별 전체 라인 개수
total_lines_count_source=count_lines_on_remote_server(**source_server)
total_lines_count_destination=count_lines_on_remote_server(**destination_server)
# 서버별로 파일 수와 용량 계산
total_files_count_source = count_files_on_remote_server(**source_server)
total_files_count_destination = count_files_on_remote_server(**destination_server)

total_files_amount_source = filesamount_on_remote_server(**source_server)
total_files_amount_destination = filesamount_on_remote_server(**destination_server)
