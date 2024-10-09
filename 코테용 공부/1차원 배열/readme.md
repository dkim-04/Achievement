# 문제

## 1번
https://www.codetree.ai/missions/4/problems/play-with-array?&utm_source=clipboard&utm_medium=text
```
n,q=map(int,input().split()) # n 원소 개수,q:질의 개수
nn=list(map(int,input().split())) # n개의 원소 리스트 

for i in range(q): # q개의 질의 반복
    qq=list(map(int,input().split()))
    que=qq[0] # 1번 답번: a번째 원소
    if que==1:
        print(nn[qq[1]-1])
    elif que==2: # 2번 답변
        for j in range(n):
            if nn[j]==qq[1]:
                print(j+1)
                break
        else:
            print(0)

    else:
        for j in range(qq[1], qq[2]+1):
            print(nn[j-1],end=' ')
        print()
```

## 2번
n1개의 원소로 이루어져 있는 수열 A의 정보와, n2개의 원소로 이루어져 있는 수열 B의 정보가 주어졌을 때 수열 B가 수열 A의 연속부분수열인지를 판단하는 프로그램을 작성해보세요.

수열 B가 수열 A의 원소들을 연속하게 뽑았을 때 나올 수 있는 수열이라면 연속부분수열이라 부릅니다.

예를 들어 수열 A가 [1, 5, 2, 6] 일때 수열 B가 [5, 2]라면 수열 B는 수열 A의 연속 부분 수열이지만, 만약 수열 B가 [5, 6]이라면 연속 부분 수열이 아닙니다.

입력 형식
첫 번째 줄에 수열 A의 원소의 개수를 나타내는 n1과 수열 B의 원소의 개수를 나타내는 n2값이 각각 공백을 사이에 두고 주어집니다.

두 번째 줄에는 수열 A에 해당하는 n1개의 원소가 공백을 사이에 두고 주어집니다.

세 번째 줄에는 수열 B에 해당하는 n2개의 원소가 공백을 사이에 두고 주어집니다.

1 ≤ n1, n2 ≤ 100
1 ≤ 주어지는 원소 ≤ 100
출력 형식
수열 B가 수열 A의 연속부분수열이라면 Yes, 아니라면 No를 출력합니다.

입출력 예제
예제1
입력:

4 2
1 5 2 6
5 6
출력:

No
```
n1, n2 = map(int, input().split())  # A 원소 개수와 B 원소의 개수
A = list(map(int, input().split()))  # A 리스트 입력
B = list(map(int, input().split()))  # B 리스트 입력

found = False  # B 리스트가 A 안에 존재하는지 여부

for i in range(n1 - n2 + 1):  # A에서 B의 길이만큼 확인
    if B[0] == A[i]:  # 첫 번째 원소가 일치하는 경우
        match = True  # 일치 여부를 추적
        for j in range(1, n2):  # B의 나머지 원소들과 비교
            if B[j] != A[i + j]:  # 일치하지 않는 경우
                match = False
                break  # 더 이상 비교할 필요 없음
        if match:  # 만약 모든 원소가 일치하면
            found = True
            break  # 일치하는 부분을 찾았으므로 반복 종료

if found:
    print('Yes')  # B 리스트가 A에 존재함
else:
    print('No')   # B 리스트가 A에 존재하지 않음
```
