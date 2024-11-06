# 코드 내용 

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

**실행 결과**
## exist_line.py
- source_server와 destination의 서버 정보 코드에 입력
- 서버 별 전체 라인 수, 전체 용량, 파일 갯수 출력

**실행 결과**
## extract_sk_car.py
- 서버 내에서 sk_origin파일을 5만 라인씩 나눈 후 필요 열만 추출
-  B_cell(1~180)열에 대해 비교 연산 수행
- 결측치가 있거나 값이(0~0.4)인 행이 있을 경우 그 행들을 제외하고 추출
- 새로운 csv 파일로 저장
- 걸린 시간:7.0시간 39.0분 3초

**실행 결과**

* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_522.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_523.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_524.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_525.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_526.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_527.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_528.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_529.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_530.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_531.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_532.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_533.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_534.csv
* 파일 저장 완료: /mnt/disk/disk02/sk_car_extract_csv-ver/sk_2207_origin/2022-12-07_11_06am/2022-12-07_11_06am_part_535.csv
* 총 걸린 시간: 7.0시간 39.0분 3.5265660285949707초
