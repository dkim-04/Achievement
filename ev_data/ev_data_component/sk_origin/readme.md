# 데이터 정보
| 구분  | 전체 라인 수 |csv_파일 수| 파일 용량 | 결측치 오류만 포함한 오류 라인 수 | 유형 2번까지 포함한 오류 라인 수 | 결측치의 오류만의 오류율 | 유형 2번 포함한 오류율 |
|:-----------|:--------------|:------------|:-----------|:-------------------------------|:--------------------------------|:------------------------|:----------------------|
| sk_origin |4억2936만 735라인|  309개      |   638G     |     2억 561만 1344라인          |  2억 7315만 4098라인            |약 23.9%(시간:3시간 32분)|약 31.8%(시간:3시간 33분)|


# 1.sk_origin
## 위치(우분투 환경)
- /mnt/disk/disk02/divided_sk_car(1,2 같은 서버에 존재)
## 실행 파이썬 파일(우분투 환경)(sample_file)
-[원격 서버에서 로컬로 복사해 전처리](https://github.com/dkim-04/Achievement/blob/f21b7dbc51d84c398a868fcdb301b152c3357b88/ev_data/ev_data_component/sk_origin/code/readme.md)
## sk_origin(전체)폴더를 전처리 후 100만개씩 파케이 파일로 전환
- 4시간 10분 46초
- 50G
- 파케이 파일을 디코딩해서 읽는 데 8시간 이상을 소비하여도 매우 오래 걸리는 것을 확인하여 정지
- 용량을 줄이는 데는 유용하나 데이터를 처리하는 데 아직 pandas df으로는 읽는 속도가 매우 느린 것을 알 수 있음 


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



