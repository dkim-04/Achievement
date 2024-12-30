# 구현해 낸 상황
- 각 CSV파일은 파일명(영문부분) 필드에 대한 TIME,STEP,STEP_NAME,PARAM_ALIAS,VALUE 정보를 나타냄
- 조건1) 각 CSV파일에 대한 VALUE 데이터를 TIME 데이터에 맞게 매칭하여 병합
- 조건2) 1개로 합쳐진 CSV파일의 칼럼라인은 각 CSV파일 명의 영문부분으로 구성
- 조건3) 1개의 CSV 파일로 병합한 후 TIME 칼럼 기준으로 데이터 라인을 정렬 후 'semi_data.csv'로 출력
  

# 보완해야 할 부분




# 해결책
- 어떤 시간이든 적용되게 코드를 바꿔야 함 

## 해결
- 어떤 시간이든 데이터 안에 있기만 한다면 적용된다.
- 하지만 데이터 파일이 늘어난다면 헤더와 데이터 열이 일치하지 않게 되므로 맞게 추가해 적용해야함