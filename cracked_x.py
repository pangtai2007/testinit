# -- coding: utf-8 --
# 有一个想法：如果坐标轴是自己画的，那么相对运动应该不成问题
# 简易的自制坐标轴

import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt


vertices = []
codes = []

codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]

vertices = np.array(vertices, float)
path = Path(vertices, codes)

pathpatch = PathPatch(path, facecolor='None', edgecolor='green')

fig = plt.figure()
ax = plt.subplot2grid((1,1),(0, 0),xticks=[], yticks=[])

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.add_patch(pathpatch)
ax.set_title('A compound path')
#plt.text(0.4, 0.25, '|')
str='llll'
off=len(str)*0.01
for i in range(0,100):
    ax.plot((5*i,5*i),(0.2,0.25))
    plt.text(5*i-off, .0, i,rotation=45)
ax.plot((-50,50),(0.2,0.2))

ax.dataLim.update_from_data_xy(vertices)
ax.autoscale_view()


plt.show()