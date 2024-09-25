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
