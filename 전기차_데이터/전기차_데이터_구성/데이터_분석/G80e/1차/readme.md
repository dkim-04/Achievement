# 전기차 데이터 분석 1차 SOC변화에 따른 평균 CELL 변화
-G80e

## 발생하는 오류 유형
1. **유형1**
![image](https://github.com/user-attachments/assets/ad4f0a2f-ea3f-4474-80dc-7399881b4221)
위 그림처럼 특정 cell들이 0으로 표기되어 평균이 다른 cell들의 평균에 비해 낮은 상태로 나타난다.

**특징**
- 특정 조건에서 나타나지 않고 여러 구간에서 발생하는 것을 발견할 수 있다
- 그러므로 이 오류의 경우 발생했을 때 처리 자동화가 쉽지 않을 것으로 예측됨

2. **유형2**
![image](https://github.com/user-attachments/assets/2ca18b43-4a15-4027-80dc-ea0682043cfc)
위 그림처럼 특정 cell들이 결측되어 평균이 다른 cell들의 평균에 비해 낮은 상태로 나타난다.]

**특징**
- 유형1과 같다
- 대부분의 그래프 밖의 이상치들은 유형1과 2에 의해 발생한다.
  

4. **유형3**
![image](https://github.com/user-attachments/assets/989a953b-6ec9-4688-b37e-98bb9f8636c9)

