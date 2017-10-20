# -- coding: utf-8 --
# 理想情况应该是全屏幕定义个函数一起拖动
# 应该尝试下单个obj的拖动
# 最后实现了：屏幕上拖动，图像正常动，坐标轴只左右动

from matplotlib import pyplot as plt
import numpy as np

press = None
press1 = None
#flag = 0

def on_click(event):
    #print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #      (event.button, event.x, event.y, event.xdata, event.ydata))
    #flag = 1
    global press
    print('on_click')
    #print(line[0].get_xydata())
    x0 = line[0][0].get_xydata()[:, 0]
    y0 = line[0][0].get_xydata()[:, 1]
    press = x0, y0, event.xdata, event.ydata

    global press1
    x1 = line[1][0].get_xydata()[:, 0]
    y1 = line[1][0].get_xydata()[:, 1]
    press1 = x1, y1, event.xdata, event.ydata
    #print('press', press)


def on_motion(event):
    #print('press', press)
    if press is None:
        return
    if event.inaxes != line[0][0].axes:
        return

    #print('on_motion')
    x0, y0, xpress, ypress = press
    dx = event.xdata - xpress
    dy = event.ydata - ypress
    line[0][0].set_data([x0 + dx, y0 + dy])
    line[0][0].figure.canvas.draw()

    x1, y1, xpress1, ypress1 = press1
    dx1 = event.xdata - xpress1
    dy1 = event.ydata - ypress1
    line[1][0].set_data([x1 + dx, y1])
    line[1][0].figure.canvas.draw()

def on_release(event):
    global press
    print('on_release')
    press = None
    line[0][0].figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
line = []
line0 = ax.plot([1,2,4,2,1])
line1 = ax.plot([0,0,0,0,0])
line.append(line0)
line.append(line1)
#print(line)
#print(line[0])
#print(line[1])


cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
cid2 = fig.canvas.mpl_connect('motion_notify_event', on_motion)
cid3 = fig.canvas.mpl_connect('button_release_event', on_release)

plt.show()

