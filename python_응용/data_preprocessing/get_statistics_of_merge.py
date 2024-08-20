###
### semi_data값 필요
###
import pandas as pd
import os
def calculate_column(file_path):
    df =pd.read_csv(file_path)
    column_medians = df.median(numeric_only=True)
    column_std = df.std(numeric_only=True)
    column_means = df.mean(numeric_only=True)
    stats_df = pd.DataFrame({
        'list': column_means.index,
        '평균': column_means.values,
        '중앙값': column_medians.values,
        '표준 편차': column_std.values
    })
    return stats_df


def save_to_csv(dataframe,output_file):
    dataframe.to_csv(output_file,index=False)

file_path ='semi_data2.csv'
output_file_path='statistics_dat.csv'

stats_df = calculate_column(file_path)

save_to_csv(stats_df,output_file_path)