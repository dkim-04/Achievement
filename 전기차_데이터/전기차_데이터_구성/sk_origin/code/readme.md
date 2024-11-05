# 코드 내용 

## division_large_file_sk.py
- 서버 ip 주소와 포트 번호, 옮길 폴더의 위치 경로, 폴더를 로컬로 옮길 경로를 입력한다
- 이후 각 csv 파일은 100만 라인씩 나뉘어져 폴더에 저장된다


## error_occured_sk_divided.py
- 서버 ip주소,서버 포트 번호, Username,password를 입력해 서버로 접근
- 이후 divided_sk_car의 데이터에서 (결측치와 0~0.4인 행 선택) 후 관련 행 선택
- 전체 파일들에서 선택된 항의 개수 및 걸린 시간 출력

## error_occured_sk_origin.py
- 서버 ip주소,서버 포트 번호, Username,password를 입력해 서버로 접근
- 이후 sk_origin의 데이터에서 (결측치와 0~0.4인 행 선택) 후 관련 행 선택
- 전체 파일들에서 선택된 항의 개수 및 걸린 시간 출력

## exist_line.py
- source_server와 destination의 서버 정보 코드에 입력
- 서버 별 전체 라인 수, 전체 용량, 파일 갯수 출력
