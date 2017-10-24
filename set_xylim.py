import matplotlib.pyplot as plt
# 尝试能不能通过改变xylim来达到改变观察的效果

global press
press=None
offset = 0.2

def on_press(event):
    print('hello')
    global xmin
    global xmax
    global ymin
    global ymax
    global ax
    if event.key == '4':
        xmin -= offset
        xmax -= offset
        ax.set_xlim(xmin, xmax)
        ax.figure.canvas.draw()
    elif event.key == '6':
        xmin += offset
        xmax += offset
        ax.set_xlim(xmin, xmax)
        ax.figure.canvas.draw()
    elif event.key == '8':
        ymin += offset
        ymax += offset
        ax.set_ylim(ymin, ymax)
        ax.figure.canvas.draw()
    elif event.key == '2':
        ymin -= offset
        ymax -= offset
        ax.set_ylim(ymin, ymax)
        ax.figure.canvas.draw()

fig = plt.figure()
global ax
ax = plt.subplot2grid((1,1), (0,0))
ax.plot([5,2,4,3,9,5,7,6,8,2,4,6,8,1])
global xmin
xmin = 3
global xmax
xmax = 5
ax.set_xlim(xmin,xmax)
global ymin
ymin = 4
global ymax
ymax = 9
ax.set_ylim(ymin, ymax)
cid1 = fig.canvas.mpl_connect('key_press_event', on_press)


plt.show()