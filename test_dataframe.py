# -- coding: utf-8 --
import pandas as pd

df = pd.read_csv('trade_toolkits/data/14_incontinuous.csv')
df = df[["time", "open", "high", "low", "close"]]
df = df[0:5]
print(df)
'''
这样把df也改掉了，这不是希望的
df2 = df
df2['open'][0] = 1
'''
'''
这样可以，不过不能操作
df2 = pd.read_csv('trade_toolkits/data/14_incontinuous.csv')
df2 = df2[["time", "open", "high", "low", "close"]]
df2 = df2[0:5]
'''
# 这个方法可行，copy决定df2是否占用新的内存
df2 = pd.DataFrame(df, copy=True)
#df2['open'][0] = 1
df2.loc[0,'open']=1

print(df2)
print(df)
