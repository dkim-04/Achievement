# 전기차 데이터 구성
## 1. 전기차 데이터 분석 과정
- sk 전기차 데이터 분석 과정

## 현재 진행 상황
1. 전기차 raw_data에서 필요한 데이터만 추출 후 새로운 csv파일로 저장
2. 약 180개의 cell의 전압을 날짜별로 15개 씩 묶어 plot으로 시각화
3. 날짜별로 충/방전 구간 나눠서 저장

## 필요한 것
1. 충/방전 구간에 따른 차 속도 온도 변화 정도 나타내기
2. pack과 모듈에서의 데이터 변화정도에 대한 코드도 필요함
3. 현재는 일일이 csv파일을 찾아서 그에 대한 폴더를 생성하는 코드이므로 내가 코드를 작동시켰을 때 모든 csv파일을 폴더별로 나눠서 저장할 수 있는 코드가 필요함 [x]

 (이는 데이터의 양이 많으므로 가장 나중에 바꿀 수 있게 할 것이다)

4. 전류와 전압의 변동성에 대한 데이터도 만들 필요가 있음
5. 전기차가 충전할 때 이론상 어떻게 되는지에 대해 정리 필요
6. 이후 배터리 온도에 관해 정리

## 가장 빠르게 진행할 것
1. [x] 원래 데이터에서 soc를 구간별 분류하고 그에 따른 cell의 변화 정도 측정 (평균)
## 데이터 분석하면서 찾은 것
### G80e
1. 급속 충전 시 약 82%에서 83%이상부터 에너지 충전 효율이 낮아지고 87%정도에서부터 다시 충전 효율이 좋아지다가 약 88~90%에서부터는 서서히 충전 효율이 낮아지는 것을 확인할 수 있다.

## 충방전 시 이론
1. **금속 충전 시 변화**
- 전압(전압은 빠르게 상승, 초기 충전 구간에서 급격하게 증가,후반부로 갈수록 전압 증가율 감소)
- 전류(1C이상의 충전률을 사용, 셀 내부 저항에 의해 상당한 열 발생시킴,따라서 전류가 클수록, 배터리 내 손실 발생하며,충전 끝날수록 전류 감소)
- 온도( 급속 충전은 셀 내부에서 많은 열 발생시키며, 배터리 온도가 급격하게 상승
- 압력(셀 내부에서 전해질 분해가 가속화
2. **완속 충전 시 변화**
- 전압(급속 충전과 유사하게 상승, 전압 변화 더 완만함)
- 전류(발열이 더 적음, 온도 변화가 더 적음)
- 온도(온도 상승이 더 크지 않음,장기적으로 배터리 수명에 이점 제공)
- 압력(셀 내부 압력 변화 거의 발생하지 않음, 전해질 분해나 가스 발생이 급속 충전에 비해 적음)
3. **방전 시 변화**
- 전압(배터리 전압 감소, 전기차가 고출력 요구하면 전압 급격히 감소 가능)
- 전류(주행 조건 따라 다름)
- 온도(고출력 방전 시 온도 급격히 상승 가능, 이를 BMS에서 모니터링해 과열 방지, 필요 시 냉각 시스템 활성화)
- 압력(심각한 방전 상태에서는 셀 내부 불균형 발생해 압력 증가 가능)

### 요약
1. 급속 충전
- 전압과 전류가 급격히 증가하고 온도와 압력이 상대적으로 많이 상승
2. 완속 충전
- 전압과 전류의 변화가 느리고 온도와 압력 상승이 적어 배터리 수명에 긍정적인 영향 미침
3. 방전
- 전압 전류 감소, 방전 속도에 따라 온도와 압력 변화 나타남
- 과방전은 배터리 손상위험 큼
