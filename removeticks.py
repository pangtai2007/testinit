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
ax = plt.subplot2grid((1,1),(0, 0))
ax.spines['left'].set_visible(False)
ax.set_xticks([])
plt.show()