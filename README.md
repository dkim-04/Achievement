# Achievement
논문 분석 및 코드 자료 업로드
=====================
## python os module(파이썬 os 모듈)
-os.mkdir 새로운 한개의 폴더 또는 경로 생성
-os.makedirs--- ./a/b/c처럼 원하는 만큼 디렉토리 생성 가능


- os.path.isdir--- 디렉토리 형식의 파일의 존재 여부를 확인하고 그에 따라 존재하면 참, 반대면 거짓을 리턴해준다
- os. path.isfile-- 위의 비슷한 역할을 하지만 파일 형식이다.
파일 확장자(filename extension)--- 컴퓨터 파일의 이름에서 파일의 종류와 그 역할을 표시하기 위해 사용하는 부분(확장자라고 부름) 운영체제들은 파일 이름에서 (.)뒤에 나타나는 부분을 확장자로 인식
-os.path.splitext---  확장자와 그 전까지의 파일 이름을 분리해 반환
-os.path.basename---path의 기본 이름을 반환합니다.
-os.path.join---여러 개의 경로를 하나의 경로로 결합할 때 사용
ex)
import os
path = os.path.join('folder1', 'folder2', 'file.txt')
print(path)
--결과
"folder1/folder2/fi.txt
-------------------------------------------------------------
open() 함수
--파일을 열고 파일 객체를 반환하는 함수
사용후 close)_메서드 호출해 파일 닫아야 함
with 사용하면 자동으로 닫을 수 있음
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzU0MjE0NDQ4LDE0ODg2OTMyNF19
-->