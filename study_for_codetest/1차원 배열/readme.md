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
https://www.codetree.ai/missions/4/problems/contiguous-array-or-not?&utm_source=clipboard&utm_medium=text
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
