# 기본 요소

## 목차
1. 변수
2. 조건문(if문)
3. 반복문(for,while,until)
4. 함수
5. 입출력 리다이렉션
6. 파이프(|)
7. 주석


### 1. 변수
- sh에서 변수는 값을 저장하고 사용할 수 있는 공간으로, 변수를 정의할 때는 등호(=)를 사용하며, 값은 공백 없이 지정해야 함

ex)
``` ruby
Name='John'
echo $NAME
```

![image](https://github.com/user-attachments/assets/737e9dc1-4603-4b74-bfcd-e58eb628c69e)


![image](https://github.com/user-attachments/assets/b5180e7c-8afc-465b-aa6d-515f517ff097)



### 2. 조건문(if문)
- if 문은 조건을 확인하고 그에 따른 명령 실행


ex)
``` ruby
if [조건]; then
elif
else
fi
```

![image](https://github.com/user-attachments/assets/d7d63cf9-d05a-48ba-b7e8-7fecc778d765)

### 3. 반복문
- for 변수 in 리스트; do

### 4. 함수
- 함수를 정의하며 호출하여 스크립트 재사용
- 호출 방법: 함수 그자체


### 5. 입출력 리다이렉션
- (>) 출력을 파일로 리다이렉션(덮어쓰기)
- (>>) 출력을 파일에 추가
- (<) 파일에서 입력 읽기





### 6. 파이프
- 한 명령의 출력을 다른 명령의 입력으로 연결

  
### 7. 주석
- sh 스크립트에서 주석은 #을 사용해 작성

