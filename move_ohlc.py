import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

fig = plt.figure()
ax = plt.subplot2grid((1,1), (0,0))
r = patches.Rectangle((0.2,0.2),0.5,0.5, fill=False, transform=ax.transAxes, clip_on=False)
ax.add_patch(r)  # 画完要add才会有

xy = r.get_xy()
#print(xy)  # xy is a tuple
#print(xy[0])
x = xy[0]
y = xy[1]

# 尝试移动矩形

#time.sleep( 2 )
r.set_xy([x+0.2,y+0.2])
r.figure.canvas.draw()
plt.show()