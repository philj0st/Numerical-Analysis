import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def f(x,t):
    return np.sin(x+t)+np.cos(2*x+2*t)

[x,t] = np.meshgrid(np.linspace(0,10), np.linspace(0,np.pi))
z = f(x,t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x,t,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title(r'wave $v(x,t)=sin(x+ct)+cos(2x+2ct)$ as surface')
plt.show()