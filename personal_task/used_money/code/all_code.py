import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
######## 파일 월별 추출 함수
# CSV 파일에서 불필요한 문자 제거
def clean_data(file_path):
    df = pd.read_csv(file_path)
    for column in df.select_dtypes(include='object').columns:
        df[column] = df[column].str.replace("'", "", regex=False)
        df[column] = df[column].str.replace('"', '', regex=False)
        df[column] = df[column].str.replace(',', '', regex=False)
    df.to_csv(file_path, index=False)

# '-'가 포함된 데이터를 추출하는 함수
def extract_data(file_path, output_path):
    df = pd.read_csv(file_path)
    filtered_df = df[df['amount'].astype(str).str.contains('-', na=False)]
    filtered_df.to_csv(output_path, index=False)

# 월별 데이터를 나누고 특정 단어가 포함되지 않은 거래 구분 필터링 후 저장하는 함수
def change_str_to_int(file_path, base_dir):
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'])
    df['year_month'] = df['time'].dt.to_period('M')

    os.makedirs(base_dir, exist_ok=True)

    selected_columns = ['time', 'amount', '거래구분']
    for name, group in df.groupby('year_month'):
        # 거래 구분에서 특정 단어 필터링
        filtered_group = group[~group['거래구분'].str.contains('저금통|세이프박스',case=False ,na=False)]
        month_dir = os.path.join(base_dir, str(name))
        os.makedirs(month_dir, exist_ok=True)
        file_name = f"{month_dir}/{name}_결제_내역.csv"
        filtered_group[selected_columns].to_csv(file_name, index=False)
        print(f"{file_name} 저장됨")
######## 병합 함수
# 여러 CSV 파일을 병합하여 하나의 파일로 저장하는 함수
def merge_csv_to_output(folder_path, output_file):
    # 모든 CSV 파일 검색
    file_paths = glob.glob(os.path.join(folder_path, '**/*.csv'), recursive=True)

    dataframes = []
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            # 'time'과 'amount' 컬럼이 있는지 확인
            if 'time' in df.columns and 'amount' in df.columns:
                df['time'] = pd.to_datetime(df['time'])  # 'time'을 datetime으로 변환
                dataframes.append(df)
        except Exception as e:
            print(f"파일 읽기 오류 {file_path}: {e}")

    if dataframes:
        # 모든 데이터프레임 병합
        merged_df = pd.concat(dataframes, ignore_index=True)
        # 'time'으로 데이터 정렬
        merged_df.sort_values(by='time', inplace=True)
        # 결과를 CSV 파일로 저장
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        merged_df.to_csv(output_file, index=False)
        print(f"병합된 파일이 저장되었습니다: {output_file}")
    else:
        print("병합할 데이터가 충분하지 않습니다.")

# 사용 예제
if __name__ == "__main__":
    # 데이터 정리 및 추출
    clean_data('../all_data.csv')
    extract_data('../all_data.csv', '../extract.csv')

    # 월별 데이터 나누기 및 필터링 후 저장
    base_directory = '../data/2024'
    change_str_to_int('../extract.csv', base_directory)

    # 저장된 월별 데이터를 병합
    output_file = '../data/output/output.csv'
    merge_csv_to_output(base_directory, output_file)
else:
    print("모듈로 적용됨")



###### 전체 그래프로 나타내는 함수


# 파일 불러오기
file_path_new = '../data/output/output.csv'
folder_path='../data/output/png_files'
def bar(file_path_new,folder_path):

    data_new = pd.read_csv(file_path_new)

    # 'time' 열을 datetime으로 변환하여 월을 추출
    data_new['time'] = pd.to_datetime(data_new['time'])

    # 'amount' 값의 음수를 제거하여 절대값으로 변경
    data_new['amount'] = data_new['amount'].abs()

    # 월별로 그룹화하고 'amount' 총합 계산
    data_new['month'] = data_new['time'].dt.to_period('M')
    monthly_data_new = data_new.groupby('month')['amount'].sum().reset_index()

    # 월별 총액을 금액 단위로 표현한 막대 그래프
    plt.figure(figsize=(10,6))
    plt.bar(monthly_data_new['month'].astype(str), monthly_data_new['amount'], color='b')
    plt.title('월별 총액 (절대값, 금액 표시)')
    plt.xlabel('월')
    plt.ylabel('총액 (원)')
    plt.xticks(rotation=45)

    # y축을 금액 단위로 포맷
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,} 원'))

    plt.grid(True, axis='y')  # y축에만 그리드 라인 추가
    plt.tight_layout()
    #png 파일로 저장
    os.makedirs(folder_path,exist_ok=True)
    png_file_path= os.path.join(folder_path,'monthly_total_amount.png')
    plt.savefig(png_file_path)
    print(f"png 파일로 저장됨{png_file_path}")
              
bar(file_path_new,folder_path)