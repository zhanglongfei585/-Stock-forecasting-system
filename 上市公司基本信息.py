import tushare as ts
import pandas as pd
import csv
import numpy as np
ts.set_token('28b14671d4afda56243c7f44256b88b9757120f3d48e01a948b45b13')
pro = ts.pro_api()
#获取上市公司基本信息
df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
df.to_csv('D:\company.csv')




