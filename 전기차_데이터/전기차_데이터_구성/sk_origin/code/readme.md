# 코드 내용 

## division_large_file_sk.py
- 서버 ip 주소와 포트 번호, 옮길 폴더의 위치 경로, 폴더를 로컬로 옮길 경로를 입력한다
- 이후 각 csv 파일은 100만 라인씩 나뉘어져 폴더에 저장된다

**실행 결과**

- divided_sk_car
  - sk2110_origin
    - eVData....
      - evData...csv 
    - evdata...
  - sk2201_origin
  - ...
  - sk_2307_origin 
## error_occured_sk_divided.py
- 서버 ip주소,서버 포트 번호, Username,password를 입력해 서버로 접근
- 이후 divided_sk_car의 데이터에서 (결측치와 0~0.4인 행 선택) 후 관련 행 선택
- 전체 파일들에서 선택된 항의 개수 및 걸린 시간 출력

**실행 결과**

## error_occured_sk_origin.py
- 서버 ip주소,서버 포트 번호, Username,password를 입력해 서버로 접근
- 이후 sk_origin의 데이터에서 (결측치와 0~0.4인 행 선택) 후 관련 행 선택
- 전체 파일들에서 선택된 항의 개수 및 걸린 시간 출력

## exist_line.py
- source_server와 destination의 서버 정보 코드에 입력
- 서버 별 전체 라인 수, 전체 용량, 파일 갯수 출력

## extract_sk_car.py
- 서버 내에서 sk_origin파일을 5만 라인씩 나눈 후 필요 열만 추출
-  B_cell(1~180)열에 대해 비교 연산 수행
- 결측치가 있거나 값이(0~0.4)인 행이 있을 경우 그 행들을 제외하고 추출
- 새로운 csv 파일로 저장
