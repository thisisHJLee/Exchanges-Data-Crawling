import FinanceDataReader as fdr
import pandas as pd
import time

ex_rate_list = ["USD/KRW"]

for ex_rate in ex_rate_list:
    df = fdr.DataReader(ex_rate, "2021-05-01", "2022-05-02")
    df.reset_index(inplace = True) # 날짜 인덱스를 컬럼으로 변경
    #df.to_csv("{}.csv".format(ex_rate.replace("/", "-"), index = False))
    df1 = df.reindex(['Date', 'Close', 'Open'], axis=1) # 필요한 열 추출
    #df1.to_csv("{}.csv".format(ex_rate.replace("/", "-"), index = False))
    df1.to_csv("{}-pro.csv".format(ex_rate.replace("/", "-"), index = False)) # csv 파일로 변환