# 데이터 정보
| 구분  | 전체 라인 수 |csv_파일 수| 파일 용량 | 결측치 오류만 포함한 오류 라인 수 | 유형 2번까지 포함한 오류 라인 수 | 결측치의 오류만의 오류율 | 유형 2번 포함한 오류율 |
|:-----------|:--------------|:------------|:-----------|:-------------------------------|:--------------------------------|:------------------------|:----------------------|
| sk_origin |8억 5872만 1470|  309개      |   638G     |     2억 561만 1344라인          |  2억 7315만 4098라인            |약 23.9%(시간:3시간 32분)|약 31.8%(시간:3시간 33분)|
|divided_sk  |8억 5872만 2082|  615개      |   405G     |     2억 561만 1344라인          |  2억 7315만 4023라인            |약 23.9%(시간:3시간 8분)|약 31.8%(시간:1시간 49분)|
|parquet_divided|8억 5872만 1470|...|50G|| |||


# 1.sk_origin
## 위치(우분투 환경)
- /mnt/disk/disk02/divided_sk_car(1,2 같은 서버에 존재)
## 실행 파이썬 파일(우분투 환경)(sample_file)
-[원격 서버에서 로컬로 복사해 전처리](https://github.com/dkim-04/Achievement/blob/23535d4aa4b87a5f70dc7b9bfbf68d77ac62d216/ev_data/ev_data_component/sk_origin/code/readme.md)

## sk_origin(전체)폴더를 전처리 후 10000만개씩 파케이 파일로 전환
- 4시간 10분 46초
- 50G
- 파케이 파일을 디코딩해서 읽는 데 8시간 이상을 소비하여도 매우 오래 걸리는 것을 확인하여 정지
- 용량을 줄이는 데는 유용하나 데이터를 처리하는 데 아직 pandas df으로는 매우 느린 것을 알 수 있음 


## sh을 통해 접근 및 실행
```markdown
#1. 외부 서버로 접근
ssh <username>@<서버 ip 주소> -p<포트번호>
```

```markdown
#2. sK_origin 전체 csv파일 갯수
find /mnt/disk/disk02/sk_origin -name "*.csv" | wc -l 
```

```markdown
#3. sk_origin 전체 용량 확인
du -sh /mnt/disk/disk02/sk_origin 
```

```markdown
#4. sk_origin의 전체 라인의 갯수
find /mnt/disk/disk02/sk_origin -name "*.csv" -exec cat {} + | wc -l 
```

```markdown
#5. sk_origin의 오류 라인 측정
python3 /mnt/disk/disk02/sk_data_code/error_occurred_sk_origin.py
```

# 2.divided_car
## 위치(우분투 환경)(sample_file)
- /mnt/disk/disk02/divided_sk_car(1,2 같은 서버에 존재)

## 실행 파이썬 파일(우분투 환경)
- [원격 서버에서 로컬로 복사해 전처리](https://github.com/dkim-04/Achievement/blob/a38e994a89be4e840c2532f7b272af703a39e55f/ev_data/ev_data_component/sk_origin/code/readme.md)
- 1시간 49분 37초

## sh을 통해 접근 및 실행
```markdown
# 1. 외부 서버로 접근
ssh <username>@<서버 ip 주소> -p<포트번호>
```

```markdown
# 2. csv파일 갯수
find /mnt/disk/disk02/divided_sk_car -name "*.csv" | wc -l 
```

```markdown
# 3. 전체 용량 확인
du -sh /mnt/disk/disk02/divided_sk_car
```

```markdown
# 4. 전체 라인 갯수
find /mnt/disk/disk02/divided_sk_car -name "*.csv" -exec cat {} + | wc -l 
```

```markdown
# 5.오류 라인 측정
python3 /mnt/disk/disk02/sk_data_code/error_occurred_sk_divided.py
```

### 데이터 정보
  (이 문제는 수치에 유의미하게 영향을 끼치지 않기 때문에 무시하고 갈 수 있다고 판단)
- (수정된 오류 라인 수): 2억 7315만 4023라인(75개 차이남)
  (걸린 시간): 3시간 10분 24초
- 위 sk_origin과 결측치만 놓고 비교 했을 때는 둘다 오류 라인이 2억 561만 1344라인으로 똑같다(읽을 때 오류 발생 X)
-  결측치의 오류만 이용했을 때의 오류율: 약 23.9%
-  유형2를 포함했을때의 오류율:약 26.7%
-  수정된 오류율:약 31.8%

## 유형2
- 데이터를 보니 내가 넣은 조건은 열에서 전 행이 1.5보다 클때 후 행이 0일때만 조건이 작동한다
- 하지만 생각해보니 연속으로 0이 나오는 경우 이 가정이 작동하지 않으므로 이 조건과 0.01~0.03이 될 때도 있으니 이 조건을 어떻게 넣을지에 대해 고민해 적용해야 함
- 해결책: 전행이 결측인 경우에도 0.1~0.4인 경우 처리하게 설계, 유형 3번의 경우 위 두가지 조건이 만족되지 않을 때 soc를 봐야 하기 때문에 데이터를 차종별로 전처리 후 오류를 찾아야 함


# sk_origin을 divided_car로 전처리하기
## 실행하는 파이썬 스크립튼(우분투 버전), (외부 환경에서 로컬로)/ 외부 환경만 이용한 버전은 만드는 중
- [sk_origin을 100만 라인씩 전처리](https://github.com/dkim-04/Achievement/blob/3b961503e731cbc400c5178d289efc1cff657017/%EC%A0%84%EA%B8%B0%EC%B0%A8_%EB%8D%B0%EC%9D%B4%ED%84%B0/%EC%A0%84%EA%B8%B0%EC%B0%A8_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EA%B5%AC%EC%84%B1/sk_origin/code/division_large_file_sk.py)
