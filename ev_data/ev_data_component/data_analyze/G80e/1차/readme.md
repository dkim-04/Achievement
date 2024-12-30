# 전기차 데이터 분석 1차 SOC 변화에 따른 평균 CELL 변화
-G80e

## 발생하는 오류 유형


### 1. **유형1**
![image](https://github.com/user-attachments/assets/2ca18b43-4a15-4027-80dc-ea0682043cfc)

위 그림처럼 특정 cell들이 결측되어 평균이 다른 cell들의 평균에 비해 낮은 상태로 나타나는 경우

**특징**
- 유형1과 같다
- 대부분의 그래프 밖의 이상치들은 유형1과 2에 의해 발생한다.
  

### 2. **유형2**

![image](https://github.com/user-attachments/assets/3f51222d-e01b-4a2a-9d4c-b23b5770ef46)

위 그림처럼 soc 값과 온도,전압이 매우 커지는 값이 나오게 되는 경우

**특징**
- 측정 시간의 텀을 두고 측정할 때와 일반적인 진행상황 두 상황 모두 발생하는 것을 확인할 수 있다.
- 팩전압과 온도가 매우 큰 수치를 나타내는 것을 확인할 수 있다.(온도가 140~200 사이로 나오는 것을 통해 오류인 것을 알 수 있다)
- CELL의 평균이 결측으로 인해 매우 낮은 수치로 발생하는 것을 확인할 수 있다.
- 다른 오류들과 다르게 아래의 그림들과 같이 일정 구간에서 발생, 비슷한 그래프를 그린다는 것을 알 수 있다.
- 다른 오류들 같은 경우, 발생 환경,조건이 일정하지 않아 이상치를 자동처리화하기 쉽지 않지만, 이 유형의 경우 발생 조건이 일정하다
- 이 유형은 SOC가 (86%-100%)사이에서 발생하며, 평균 CELL은 최소 (2.5-2.6)사이에서 시작되며, 그 보다 낮은 수로는 나타나지 않는다
- 그래프 유형은 아래의 원과 같이 나타난다.

***참고***
- 여러가지 조건을 종합한 결과, 이 유형의 경우 일정하게 발생하는데는 BMS가 일정하게 오류를 발생시키는 것으로 생각되고, 이를 통해 유형2의 경우의 값들을 제외하고 진행한다면 EV데이터 분석의 시간과 양을 단축시킬 수 있을 것이라고 생각된다.
- 아래의 그래프들의 경우 모두 같은 차종의 다른 모델들의 실험결과들이다.

   
![changed_M221003864](https://github.com/user-attachments/assets/063e6ef4-fac5-408e-8e34-f3e04376a6e1)
![changed_M2210703932_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/c3e6475e-eb78-418c-b81c-a1ccd7dc4ff2)
![changed_M2210703934_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/bb0045c6-1572-4b82-abf5-2df425251f84)
![changed_M2210703935_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/b842d931-143c-4db7-848f-b9f32f6f8b64)
![changed_M2210703936_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/a4aed7fa-98bd-4aa1-93ff-160e9f5de578)
![changed_M2210703938_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/e6c8340f-dcc9-48d0-8424-db76df71d4c0)
![changed_M2210703944_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/09f4383d-8a3f-40b0-9aa3-3a9c44b2da24)
![changed_M2210703945_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/0c5f52b1-b4d5-4062-9600-7df4876c0b4c)

***위 그림이 이 유형의 가장 대표적인 예시이다.***
- 위 그림의 경우 일반적인 값의 경우 90%-100%의 값이 존재하지 않고, 오류 유형으로써의 값만 존재한다.


![changed_M2210703946_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/ae0e4b4c-3a5e-4fef-be23-4663bc80c05f)
![changed_M2210703947_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/190c102e-0ab6-4840-8b55-7d0ced560b91)
![changed_M2210703948_soc_vs_voltage_scatter_10percent_intervals](https://github.com/user-attachments/assets/f3b92e48-1582-470f-8983-c2fbf18b0522)
