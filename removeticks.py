# -- coding: utf-8 --
# 不均等子图尺寸的另一个例子，应该模仿这个来做
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

#dt = 0.01
#t = np.arange(0.0, 10.0, dt)
#r = t+1 # impulse response
#print(r)
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
# 只有在构造时把yticks设置为空才能隐藏y轴刻度及数字，而set_yticks是没用的，原因不明
ax1 = plt.subplot2grid((1,2),(0, 1),yticks=[])
#ax1.set_xticks([])
ax.spines['left'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax.set_xticks([])
plt.show()