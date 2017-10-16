# -- coding: utf-8 --
# 有一个想法：如果坐标轴是自己画的，那么相对运动应该不成问题
# 简易的自制坐标轴

import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import trade_toolkits.visual.plot2
#import trade_toolkits.environments.market_db as md
import pandas as pd
import matplotlib.pyplot as plt
import time
import random


a1=(1976,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(1990,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

#随机生成10个日期字符串
date_l = []
for i in range(10):
    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    date_l.append(date)
    #print(date)

fig = plt.figure()
ax = plt.subplot2grid((1,1),(0, 0), xticks=[], yticks=[])
ax.set_aspect(1)

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xlim(-100,100)

off=2
for i in range(-3,3):
    ax.plot((15*i,15*i),(0,1))
    plt.text(15*i-off, -5, date_l[i+3],rotation=45)

ax.plot((-200,200),(0,0))
#ax.plot((0,0),(-100,100))
ax.plot((-100,100),(-100,100))
#ax.set_title('A date xaxis')

#ax.set_aspect(1)
if __name__ == '__main__':
    #candlestick_plot = visual.plot.CandlestickPlot("data/14_incontinuous.csv", "data/trader.csv")
    #candlestick_plot.plot()
    candlestick_plot = trade_toolkits.visual.plot2.CandlestickPlot("trade_toolkits/data/14_incontinuous.csv", "trade_toolkits/data/trader.csv")
    candlestick_plot.plot()


plt.show()