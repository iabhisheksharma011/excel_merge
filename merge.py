import os
import pandas as pd
import datetime

dt = str(datetime.datetime.now())
dt1 = dt[0:10]

sheet = "CONSOLIDATED COVID DATA.xlsx"
df = pd.concat(pd.read_excel(sheet, sheet_name=None), ignore_index=True)

df.to_excel("CONSOLIDATED COVID DATA_.xlsx")

newname = 'CONSOLIDATED COVID DATA_'+dt1+'.xlsx'
os.rename('CONSOLIDATED COVID DATA_.xlsx', newname)
