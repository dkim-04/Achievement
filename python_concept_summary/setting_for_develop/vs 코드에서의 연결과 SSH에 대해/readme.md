# vs 코드에서의 연결 차이와 SSH에 대해서
## vs 코드에서 인터프리터를 사용하는 경우
### 목적
- 코드 실행
- 디버깅
- 통합 개발 환경(IDE) 기능:

## vs 코드에서 터미널을 이용해 SSH 연결하는 경우
- 원격 서버 접속
- 서버 관리
- 원격 개발

## 차이점
* VS code 인터프리터:
  - 로컬 환경에서 코드 실행 및 디버깅
  - 주로 코드 작성 및 테스트에 사용
* VS code 터미널에서 SSH 사용:
  - 원격 서버에 접속하여 서버 관리 및 원격 개발 작업 수행
  - 원격 환경에서의 작업과 로컬 컴퓨터에서의 작업을 구분하여 사용할 수 있음
 
## 결론
- 인터프리터는 주로 로컬에서 코드를 실행하고 디버깅하는 데 사용됨
- SSH를 사용하는 것은 원격 서버에 접속하여 관리하거나 원격 개발을 수행하는 데 사용됨

## SSH란 무엇인가?
- (Secure Shell)SSH는 네트워크를 통해 컴퓨터에 안전하게 접속하고 원격으로 시스템을 관리하거나 명령을 실행하기 위해 사용되는 암호화된 통신 프로토콜이다.
- 원격 서버에 로그인하거나 명령어를 실행할 때 보안 강화하기 위해 사용
- 데이터를 암호화해 전송하기 떄문에 도청,위장,중간자 공격등을 방지 가능

### 특징
1. 보완성
2. 원격 로그인 및 명령어 수행
3. 포트 포워딩:Port Forwarding
  - 네트워크 내에서 안전한 터널을 통해 데이터를 전송 가능
  - SSH 터널링을 설정해 특정 포트를 통해 안전하게 다른 네트워크 서비스에 접근 가능
4. 파일 전송 안전하게 가능
5. 대칭 암호화와 비대칭 암호화 사용

### SSH 구성 요소
1. SSH 클라이언트
  - 사용자 컴퓨터에서 실행되며, SSH 서버에 연결하여 세션 시작
  - 리눅스와 mac에는 기본적으로 SSH가 설치되어 있으며 windows에서도 기본적으로 설치된 OpenSSH 클라이언트를 사용할 수 있음
2. SSH 서버
  - SSH 서버는 원격 컴퓨터에서 실행되며, 클라이언트의 연결을 기다림
  - 사용자가 SSH 클라이언트를 통해 서버에 접속하면, 서버는 사용자의 자격 증명을 확인하고 접속을 허가
3. SSH 키
  - SSH 접속을 위해 사용하는 인증 방법 중 하나로, 공개 키(public key)와 개인 키(private key)로 구성된 SSH 키 페어를 사용

### SSH 작동 방식
1. 클라이언트-서버 모델
  - 클라이언트가 서버에 연결을 시도하면, 서버는 클라이언트에게 자신의 공개 키를 보냄
2. 인증 및 암호화
  - 서버의 공개 키를 사용해 데이터를 암호화하고, 서버는 자신의 개인 키를 사용해 데이터를 복호화해 클라이언트 인증
  - 인증이 종료되면, 양측은 안전한 세션 키를 생성해 데이터를 암호화하고 전송 시작
