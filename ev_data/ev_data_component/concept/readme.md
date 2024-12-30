# 중요 개념
1. soc(State of Charge)
  - 배터리 현재 충전 상태
2. BMS(battery management system)
  - 배터리 성능 최적화 및 안전하게 운영하기 위해 필수적인 장치

## 전지(Battery란?)
![image](https://github.com/user-attachments/assets/828eb60b-cdee-41bd-aad7-91134065ebbf)
![image](https://github.com/user-attachments/assets/052ecce2-128e-42a0-b89b-7f11e40bdd4c)
- **BEV**이지만 (EV라고만 하기도 한다)

![image](https://github.com/user-attachments/assets/4572a08c-3a3a-453d-9f2e-8aa6084c6a73)
![image](https://github.com/user-attachments/assets/c2a30507-8308-4e02-b945-083f98dfd79e)
![image](https://github.com/user-attachments/assets/54c2b6b1-3a62-4760-9715-ab4b6e3763cf)

## 배터리 팩
![image](https://github.com/user-attachments/assets/18c82b1a-3417-4a40-bcd5-1db5a4072547)

셀-모듈-배터리 팩

- 모듈(수많은 셀, 온도 센서,전압 측정기,절연 플레이트 등으로 구성)
- 전압과 온도 센싱 가능
![image](https://github.com/user-attachments/assets/f1d5b2b1-09da-4f56-bc88-44f0d47d76aa)

- 배터리 팩(모듈들과 BMS,냉각 장치와 같은 보조 장치들로 구성)
![image](https://github.com/user-attachments/assets/b4aa31cd-46c9-4f95-ae07-83f1a57efdd8)

- BMS(팩에서 가장 핵심적인 부품)
- 전압, 전류, 온도 이상을 감지할 경우 충전과 방전을 중단시키는 등의 안전장치가 포함된 장치
- 차량과 배터리 소프트웨어 간의 원할한 통신 형성해 배터리 교체 시기와 문제를 사전에 예측
![image](https://github.com/user-attachments/assets/76c81894-01f2-4010-a604-6db532035950)

### 배터리 팩 주요 역할
1. 배터리 셀 전압, 전류 및 온도의 모니터링
2. SOC 계산
3. 배터리 시스템 진단
4. 냉각 장치 제어

## 배터리 팩과 셀 전체 평균의 차이점
1. 셀 전체 평균 전압:
* 정의: 배터리 팩에 포함된 모든 셀의 전압을 평균한 값
* 의미: 셀들이 얼마나 균일하게 충전되었는지를 보여줌.셀 전압이 고르게 분포되어 있는지 확인하는 데 사용되며, 큰 편차가 있으면 셀 밸런싱이 필요할 수 있음

2. 팩 전압:
* 정의: 배터리 팩의 총 전압으로, 팩 안의 셀들이 직렬 또는 병렬로 연결된 상태에서 측정한 전체적인 전압

* 의미: 배터리 팩이 제공할 수 있는 전압을 의미하며, 전체 시스템에서 사용할 수 있는 전압을 나타냅니다.

3. 차이점:
* 측정 위치: 셀 전체 평균 전압은 개별 셀들의 전압을 평균한 값이고, 팩 전압은 배터리 팩의 단자에서 측정된 전체 전압
* 전압 손실 및 불균형: 팩 전압이 셀 평균 전압과 다른 이유는 셀 간의 전압 차이, 배터리 내부의 저항, 연결 부위에서의 전압 강하 등이 있을 수 있기 때문이다 셀 간에 불균형이 존재하면 셀
* 평균 전압이 팩 전압보다 낮거나 높을 수 있음

**요약:**

* 셀 평균 전압은 셀들 간의 상태를 나타내고, 팩 전압은 배터리 팩 전체의 상태를 나타냄
* 차이가 크면 셀 불균형이 있거나 배터리의 효율에 문제가 있을 수 있어, 관리가 필요할 수 있음



1. 셀 평균 전압을 사용하는 경우:


* 셀 간 균일성 및 밸런싱 분석: 배터리 팩 내 개별 셀의 상태를 모니터링할 때, 셀 평균 전압을 자주 사용. 특히 리튬 이온 배터리에서는 셀 간의 전압 차이가 매우 중요하기 때문에, 셀 평균 전압을 사용하여 전체 셀들이 균일하게 충전되고 있는지 확인
* 셀 불균형 감지: 셀들의 전압 차이가 크다면 배터리 관리 시스템(BMS)이 이를 감지하고 밸런싱을 시도해야 하기 때문에, 셀 평균 전압은 중요.
배터리 수명 및 성능 예측: 셀 전압이 불균형하면 배터리 수명에 영향을 미칠 수 있음. 셀 평균 전압과 개별 셀 전압 간의 차이를 통해 이런 문제를 예측 가능


2. 배터리 팩 전압을 사용하는 경우:
* 시스템 레벨의 전압 및 에너지 관리: 배터리 팩 전압은 전기차나 전력 시스템에서 중요한 성능 지표이다. 시스템이 동작하는 동안 팩 전압은 전체적으로 공급 가능한 전압을 나타내므로, 팩 전압을 모니터링하면 시스템 레벨에서 배터리 상태를 평가할 수 있음

* 에너지 용량 및 상태 추적(SOC): 배터리 팩 전압을 사용하여 배터리의 충전 상태(State of Charge, SOC)를 추정하는 경우가 많다. 팩 전압은 SOC와 직접적인 상관관계가 있으므로, SOC를 예측하거나 모니터링하는 데 유용함

결론:

* 셀 평균 전압은 개별 셀 상태 및 불균형 분석에 주로 사용됨
* 배터리 팩 전압은 전체 시스템의 전압 모니터링과 SOC 추적을 위해 많이 사용됨
* 따라서, 분석하고자 하는 데이터가 개별 셀 상태와 관련이 있다면 셀 평균 전압을 사용하고, 시스템 성능을 평가하거나 SOC를 추적하는 경우 배터리 팩 전압을 사용하는 것이 일반적
