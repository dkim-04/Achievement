# 코드 내용 
## sk_origin에서 로컬로 데이터 파일 이동시키기
**EX)**: 터미널의 아래의 코드를 입력해 로컬로 복사
```bash
rsync -avzh -e "ssh -p 7773"  dkim04@bigsoft.iptime.org:/mnt/disk/disk02/sk_origin/sk_2307_origin/sk_2307_origin.csv /mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/divided_sk_car
```

## extract_sk_car.py
-  로컬에 특정 폴더로 옮겨진 모든 csv파이들을 5만 라인씩 나눈 후 필요 열만 추출
-  B_cell(1~180)_Volt열에 대해 비교 연산 수행
- 결측치가 있거나 값이(0~0.4)인 행이 있을 경우 그 행들을 제외하고 추출
- 새로운 csv 파일로 저장
- 걸린 시간:8분 20초

**실행 결과**
* 파일 저장 완료: /mnt/c/Users/kim/P_Ver1/car_data/sk_car_data/sk_origin/divided_sk_car/preprocessing/./sk_2307_origin/sk_2307_origin_part_(1~95).csv
* 총 걸린 시간: 0.0시간 8.0분 20.164480924606323초

## error_occured_sk_origin.py
- 로컬로 옮겨진 파일들의 전체 라인수와 오류 라인 수 측정 및 오류율 계산
- 이후 extract_sk_car.py로 나뉘어진 전체 라인 수 출력
**실행 결과**
