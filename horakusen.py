import matplotlib.pyplot as plt
import numpy as np

def f(x, t):
    return t * x - t**2

def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    return fig, ax


fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-5,5,2)
for n in range(21):
	y = f(x, t=-5+0.5*n)
	ax.plot(x, y, 'r-', linewidth=2, alpha=0.6)
plt.show()
