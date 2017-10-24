# -- coding: utf-8 --
# 有一个想法：如果坐标轴是自己画的，那么相对运动应该不成问题
# 简易的自制坐标轴

import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import trade_toolkits.visual.plot3
#import trade_toolkits.environments.market_db as md
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

#ax.set_aspect(1)
if __name__ == '__main__':
    #candlestick_plot = trade_toolkits.visual.plot.CandlestickPlot("trade_toolkits/data/14_incontinuous.csv", "trade_toolkits/data/trader.csv")
    #candlestick_plot.plot()
    candlestick_plot = trade_toolkits.visual.plot3.CandlestickPlot("trade_toolkits/data/14_incontinuous.csv", "trade_toolkits/data/trader.csv")
    candlestick_plot.plot()


plt.show()