```ruby
import time

import sys

import os

def printProgressBar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=50, fill='█'):
    
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))) ##반복
    
    filledLength = int(length * iteration // total) ## 전체 과정 반복 중 progressbar가 얼마나 차야 하는지를 보여주는 역할
    
    bar = fill * filledLength + '-' * (length - filledLength)  #█*filledLength + /"-"*(전체 length-채워져 있는 영역)=█*filledLength ////"-"* 안채워져 있는 부분
    
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    
    sys.stdout.flush() ## print() 함수의 개행 여부와 상관 없이 출력 해주는 기능

    if iteration == total:
        print()

def process_large_file(file_path):
    
    #전체 파일 라인 수 계산
    with open(file_path, 'r') as file:
        total_lines = sum(1 for _ in file)

    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            
            time.sleep(0.01)
            # progrssbar 업데이트
            printProgressBar(i, total_lines, prefix='Processing', suffix='Complete', length=50)
```
