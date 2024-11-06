###
### semi_data값 필요
###
import pandas as pd
import os

# 각 열의 항들을 계산하는 코드
def calculate_column(file_path):
    df =pd.read_csv(file_path)  # file_pathd의 csv파일을 읽는다. 
    column_medians = df.median(numeric_only=True)  # 열의 중앙값 구하기
    column_std = df.std(numeric_only=True)  # 열의 표준편차
    column_means = df.mean(numeric_only=True) # 열의 평균
    stats_df = pd.DataFrame({    # 이를 stats_df라는 데이터프레임으로 저장
        'list': column_means.index,
        '평균': column_means.values,
        '중앙값': column_medians.values,
        '표준 편차': column_std.values
    })
    return stats_df

# 계산 후 데이터 프레임을  다른 이름의 csv로 저장  
def save_to_csv(dataframe,output_file):
    dataframe.to_csv(output_file,index=False)

file_path ='semi_data2.csv'
output_file_path='statistics_dat.csv'

stats_df = calculate_column(file_path)

save_to_csv(stats_df,output_file_path)
