# wsl에서의 django 환경 준비

1. wsl 설치 및 wsl에 가상환경 준비

**가상환경을 사용하는 이유**

1. python 프로젝트 간의 패키지 버전 충돌을 방지
2. 프로젝트마다 필요로 하는 종속성 독립적으로 관리(특정 프로젝트에서만 필요한 페키지 설치하거나 제거하는 것이 용이
3. 시스템 전역 패키지 오염 방지
4. 버전 관리 편리성
5. 배포 준비에 유리
6. wsl과 windows 파일 시스템 분리


# 2. wsl 가상환경 다운로드

## 과정 코드
1. pythn3 -m venv myenv
2. source myenv/bin/activate
3. pip install django
4. (프로젝트 생성): django-admin startproject myproject
5. cd myproject
6. (앱 생성): python3 manage.py startapp myapp


ㅊㄴ![image](https://github.com/user-attachments/assets/65ce9d45-d699-42a7-97d0-4078e938d77d)
