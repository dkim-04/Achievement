# 컨테이너 기술이란?
- 애플리케이션을 환경에 구애 받지 않고 실행하는 기술
- 운영체제에서 실행되는 프로세스를 격리해 별도의 실행 환경을 제공해주며, 해당 프로세스는 운영체제 상에서 실행되는 유일한 프로세스인 것처럼 작동하는 기술
-  별도의 운영 환경을 제공해주는 기술

## 장점
- 가벼움(컨테이너의 경우 Guest os가 없기에 MB 단위의 크기를 가진다)
- 탄력성(Linux, Windows, 가상머신, Data Center, Public Cloud 등 어느 환경에서나 구동이 되므로 개발 및 배포가 크게 쉬워진다)
- 유지 관리 효율(운영 체제 커널이 하나밖에 없기 때문에 운영 체제 수준에서 업데이트 또는 패치 작업을 한 번만 수행하면 변경 사항이 모든 컨테이너에 적용된다)

이를 통해 서버를 더 효율적으로 운영하고 유지 관리할 수 있습니다.

### 가벼움
- 컨테이너의 경우 Guest os가 없기에 MB 단위의 크기를 가진다


### 탄력성
- Linux, Windows, 가상머신, Data Center, Public Cloud 등 어느 환경에서나 구동이 되므로 개발 및 배포가 크게 쉬워진다

## 컨테이너 아키텍쳐
- 격리를 담당하는 Linux Namespace와 리소스를 제어하는 Control Group(cgroup)을 사용하여 격리된 컨테이너 환경을 제공

**Namespace**

- 마운트 포인트
- 프로세스
- 네트워크 -IPC
- UtS
- 사용자


**제어 그룹**

- CPU
- 메모리
- 네트워크 대역폭
- 디스크 입출력

## 도커 컨테이너
![image](https://github.com/user-attachments/assets/18a673e9-e07a-4e1b-8252-1975c79e8eb4)
![image](https://github.com/user-attachments/assets/73e51af5-af25-4f44-ba62-c09dc241c74e)


