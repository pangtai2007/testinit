# -- coding: utf-8 --
# 应该放弃这个，因为就算成功了也不知道如何sharey
# 不如使用subplot2grid
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

#heart shape line
t=np.linspace(0,2*pi,30)
x1=6*(2*cos(t)-cos(2*t))
y1=6*(2*sin(t)-cos(2*t))
x2=3*(2*cos(t)-cos(2*t))
y2=3*(2*sin(t)-cos(2*t))

plt.figure()

#set size of subplots
left,width=0.14,0.77
bottom,height=0.11,0.5
bottom_h=bottom+height+0.05

rect_line1=[left,bottom,width,height]
rect_line2=[left,bottom_h,width,0.3]
print(rect_line1)
print(rect_line2)
axbelow=plt.axes(rect_line1)
axupper=plt.axes(rect_line2)

#plot the lines
plot1=axbelow.plot(y1,x1,'-ob',ms=3)
plot2=axupper.plot(y2,x2,'-ob',ms=3)

#setting of ax1
plt.sca(axbelow)
plt.ylim(-20,10)
plt.xlim(-20,10)
#
#
#
plt.grid(True)

#setting of ax2
plt.sca(axbelow)
#plt.ylim(-20,10)
plt.xlim(-20,10)
#
#
#
plt.grid(True)

plt.show()