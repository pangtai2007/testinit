# -- coding: utf-8 --
# 这个文件实现了单个对象的拖动
# 放置rect1,2两条折线，现在可以分别拖动，尝试使它们一起运动或者运动的有关联
from matplotlib import pyplot as plt
import numpy as np

class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.get_xydata())
        x0 = self.rect.get_xydata()[:,0]
        y0 = self.rect.get_xydata()[:,1]
        #x0 = self.rect.get_xdata
        #y0 = self.rect.get_ydata
        print('x0',x0)
        print('y0', y0)
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        #self.rect.set_x(x0+dx)
        #self.rect.set_y(y0+dy)
        self.rect.set_data([x0+dx,y0+dy])

        self.rect.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)

fig = plt.figure()
ax = fig.add_subplot(111)

#ay = np.array([0,1,2,3,4])
#print(ay)
rect1 = ax.plot([1,3,2,6,4,5])
#x=rect1[0].get_xdata
#print(x)
drs = []
for rect in rect1:
    dr = DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)

rect2 = ax.plot([2,4,3,7,5,6])
drs1 = []
for rect in rect2:
    dr = DraggableRectangle(rect)
    dr.connect()
    drs1.append(dr)

plt.show()