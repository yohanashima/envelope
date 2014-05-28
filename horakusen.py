from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid.axislines import SubplotZero

def f(x, t):
    return t * x - t**2
	
fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

ax.axhline(linewidth=1.2, color="black")
ax.axvline(linewidth=1.2, color="black")

for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
	ax.axis[direction].set_visible(False)
	
plt.figtext(0.93, 0.37, 'a')  
plt.figtext(0.505, 0.95, 'b')

plt.xticks([])
plt.yticks([])		
ylim(-3.5,6.5)

x = np.linspace(-5,5,2)
a = np.linspace(-2,2,12)
for t in a:
	y = f(x, t)
	ax.plot(x, y, 'k-', linewidth=1.0, alpha=0.6)
plt.show()
