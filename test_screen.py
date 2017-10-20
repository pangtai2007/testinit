# -- coding: utf-8 --
# 理想情况应该是全屏幕定义个函数一起拖动
# 应该尝试下单个obj的拖动
# 最后实现了：屏幕上拖动，图像正常动，坐标轴只左右动
# 把代码改成动态的，思路比较清楚
# 解决了x轴多对象的问题，但是整个移动非常的卡
# 在K线图里还要解决y轴的问题
# 已经处理了带标注的x轴问题，但是动画很卡
# 这个demo最好做成面向对象的

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

press = None
press1 = []
# 现在应该使press1应该存x轴几个对象的原点数据
# 到这里应该比较清楚了，一同移动的对象就加入一个list，在回调函数里面分别操作就好
# 把这个功能移植到plot的步骤：。。。
#flag = 0

def on_click(event):
    #print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #      (event.button, event.x, event.y, event.xdata, event.ydata))
    #flag = 1
    global press
    print('on_click')
    #print(line[0].get_xydata())
    x0 = line0[0].get_xydata()[:, 0]
    y0 = line0[0].get_xydata()[:, 1]
    press = x0, y0, event.xdata, event.ydata

    global press1
    for xline in line1:
        # 不同对象获取坐标的方法不一样
        if type(xline)==matplotlib.lines.Line2D:
            x1 = xline.get_xydata()[:, 0]
            y1 = xline.get_xydata()[:, 1]
            #press1 = x1, y1, event.xdata, event.ydata
            press1.append([x1, y1, event.xdata, event.ydata])
        elif type(xline)==matplotlib.text.Text:
            x1, y1 = xline.get_position()
            press1.append([x1, y1, event.xdata, event.ydata])
    #print('press', press)


def on_motion(event):
    #print('press', press)
    if press is None:
        return
    if event.inaxes != line0[0].axes:
        return

    #print('on_motion')
    x0, y0, xpress, ypress = press
    dx = event.xdata - xpress
    dy = event.ydata - ypress
    line0[0].set_data([x0 + dx, y0 + dy])
    line0[0].figure.canvas.draw()

    #x1, y1, xpress1, ypress1 = press1
    #dx1 = event.xdata - xpress1
    #dy1 = event.ydata - ypress1
    #line1[0].set_data([x1 + dx, y1])
    #line1[0].figure.canvas.draw()
    for i in range(0, len(press1)):
        x1, y1, xpress1, ypress1 = press1[i]
        dx1 = event.xdata - xpress1
        if type(line1[i])==matplotlib.lines.Line2D:
            line1[i].set_data([x1 + dx, y1])
            line1[i].figure.canvas.draw()
        elif type(line1[i])==matplotlib.text.Text:
            line1[i].set_position([x1 + dx, y1])
            line1[i].figure.canvas.draw()

def on_release(event):
    global press
    print('on_release')
    press = None
    global  press1
    press1 = []
    line0[0].figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)

line0 = ax.plot([1,2,4,2,1])
# 问题是，x轴不是一条线段这么简单，上面有多个对象

line1 = ax.plot((0, 4), (0, 0))
for i in range(0, 5):
    line1_xtick = ax.plot((i, i), (0, 0.1))
    line1 += line1_xtick

#print(type(line1_xtick[0]))
# 类型名matplotlib.lines.Line2D

# 加标注
for i in range(0, 5):
    line1_xtick = ax.text(i,0.2,i)
    # text取得
    #print('x,y',line1_xtick.get_position())
    line1.append(line1_xtick)

# 在坐标系中考虑标注以后有一个问题，标注随轴一起移动，但是set的方法并不一样
# 尝试是否能用type解决
#print(type(line1_xtick))
if type(line1_xtick)==matplotlib.text.Text:
    print(1)

cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
cid2 = fig.canvas.mpl_connect('motion_notify_event', on_motion)
cid3 = fig.canvas.mpl_connect('button_release_event', on_release)

plt.show()

