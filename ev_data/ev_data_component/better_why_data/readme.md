# better_why_data
- 원격 서버로 원본 파일을 rsync 이용해 옮겼을 때 용량/걸린 시간: 278.43G/49분 54초(표시되는 건 260G인데 이유는 찾지 못함-du -sh 사용)- 원본 파일에서도 260G로 표시된다.

  (라인 수를 source와 destination과 비교해 같은지 확인 예정)
- 라인수: destination_server= 2억 1330만 4547개 source_server=2억 1330만 4547개

  
- Minio client 이용해 옮겼을 때 약 5시간 걸리고 중간에 파일을 읽을 때 에러가 대략적으로 1G당 한개가 발생했다

   (그러므로 왠만하면 원격 서버를 통해 연결하는 것이 안정성과 속도 면에서 더 빠르다)

## better_why_data의 오류 경우:
차량별 데이터로 전처리 후 오류 라인 갯수 파악 후 차량 데이터 분석할 예정
