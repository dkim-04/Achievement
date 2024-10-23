# 코드 내용 설명
1. exist_line.py: 폴더 전체를 옮겼을 때 원격 서버 간 라인 갯수, 파일 수, 파일 용량을 비교해 옮길 때 오류가 없었는지 확인(server정보는 빼놓고 저장)
2. error_occured.py: csv 파일에서 발생하는 오류들의 라인을 찾아내 총 오류 라인 갯수가 몇개인지 찾아냄
3. divison_large_file.sk.py: 원본 파일에서 필요한 열만 추출하고 chunk_size=100만 라인으로 나눠 100만 라인씩 저장
  - (os.walk만 쓰게 돠면 csv파일의 바로 윗 폴더만 경로로 출력되므로 relpath 이용)
