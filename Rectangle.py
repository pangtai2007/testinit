# -- coding: utf-8 --
# 用于测试矩形

from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import matplotlib.patches as patches

global press
press=None

def on_click(event):
    global press
    #press = []
    x,y = r.get_xy()
    press = [x, y, event.xdata, event.ydata]

def on_motion(event):
    if press is None:
        return
    if event.inaxes != r.axes:
        return
    x,y,xp,yp = press
    dx = event.xdata - xp
    dy = event.ydata - yp
    r.set_xy([x + dx, y + dy])
    r.figure.canvas.draw()

def on_release(event):
    global press
    press = None

fig = plt.figure()
ax = fig.add_subplot(111)
r = patches.Rectangle((0.1,0.1), 0.5, 0.5)
print(r)
ax.add_patch(r)

cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
cid2 = fig.canvas.mpl_connect('motion_notify_event', on_motion)
cid3 = fig.canvas.mpl_connect('button_release_event', on_release)

plt.show()

