# 1. 대규모 데이터 다운로드 과정

## 1.SSH 서버를 연결하여 직접 다운로드
### 1.
- 원본 데이터가 들어 있는 서버와 내가 데이터를 넣을 서버를 연결
**연결 방법**
  1. 원본 데이터가 있는 서버에 접속(ssh id<서버주소,ip>)
  2. 이후 destination 서버로  scp -P 포트번호 -r(재귀적으로 복사) 보내려는 파일 혹은 폴더의 경로 보내려는 서버의 주소:(받는 폴더의 경로)를 이용해 파일을 보낸다
  *현재 내가 해본 다운로드 과정 중 가장 빠른 방법이라고 생각된다.*

### 2.
- wget 혹은 curl 이용

ex)wget -r -np -nH --cut-dirs=1 -R "index.html*" <URL>

## 2. EX) minio에 있는 데이터 버킷을 파이썬 파일을 이용해 다운로드

1. 원격서버에서 Minio client를 이용해 직접 복제하기
  - 원격 서버에 Minio client 설치 후 MInio를 mc에 등록 후 실행 권한 부여 후 mc를 시스템 경로에 이동시키기
  - mc alias set myminio https://minio-web.k-sw.mooo.com [ACCESS_KEY] [SECRET_KEY] 를 이용해 minio 서버를 등록시킴
  - mc cp -r /저장할 폴더 경로/ 상위폴더와 하위 폴더 모두 복사한다.
  **아직 시도는 못해봤지만 1번과 같이 가장 빠른 방법으로 예상됨**
2. 파이썬 스크립트를 이용해 복사
**주의 csv파일을 어떻게 처리하느냐에 따라서 다운로드 시간이 매우 달라질 수 있음**
  - dataframe으로 csv 파일을 읽어서 옮기기

**전체를 읽게 되면 굉장히 많은 시간이 소비됨**

  - 리스트로 전환하여 복사

*#1번 보다는 효율이 좋지 않다*

## 3. 폴더 안의 파일들을 여러 개의 청크로 나누어 병렬로 다운로드하는 스크립트를 작성하여 속도를 향상시킬 수 있음

