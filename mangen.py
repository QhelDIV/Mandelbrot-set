import cmath
import numpy as np
from matplotlib.pyplot import *
from config import *

def converge(Cx):
    temp=Cx
    lastlenth=cmath.polar(Cx)[0]
    nowlenth=0
    for i in range(0,20):
        Cx=Cx*Cx+temp
        nowlenth=cmath.polar(Cx)[0]
        if nowlenth>100:
            return False
        lastlenth=nowlenth
    return True

vx=vxmin
vy=vymin
xran=np.arange(vxmin,vxmax,xdelta)
yran=np.arange(vymin,vymax,ydelta)
print converge(complex(0,-1))
"""
xarray=[]
yarray=[]
for x in xran:
    for y in yran:
        if converge(complex(x,y)):
            xarray.append(x)
            yarray.append(y)
plot(xarray,yarray,linewidth=1.0)
show()
"""